"""
Pomodoro Timer Desktop App (Tkinter)

A beginner-friendly Pomodoro timer that helps with productivity by breaking work into 
focused intervals (typically 25 minutes) separated by short breaks (5 minutes).

Features:
- Work sessions (25 minutes by default)
- Short breaks (5 minutes by default)
- Long breaks (15 minutes after 4 work sessions)
- Visual countdown display
- Session counter
- Sound notification when timer ends
- Start, pause, and reset functionality

This file uses only Python standard library for maximum compatibility.
"""

import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
import datetime
import threading
import sys

try:
    import winsound
except ImportError:
    winsound = None


class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        root.title("Pomodoro Timer")
        root.resizable(False, False)
        root.configure(bg="#2C3E50")
        
        # Timer settings (in seconds)
        self.work_duration = 25 * 60  # 25 minutes
        self.short_break_duration = 5 * 60  # 5 minutes
        self.long_break_duration = 15 * 60  # 15 minutes
        
        # Session tracking
        self.current_session = 1
        self.sessions_until_long_break = 4
        
        # Timer state
        self.time_remaining = self.work_duration
        self.is_running = False
        self.is_work_session = True
        self.timer_thread = None
        self.stop_timer_event = threading.Event()
        
        # Fonts
        self.title_font = tkfont.Font(size=16, weight="bold")
        self.time_font = tkfont.Font(size=36, weight="bold")
        self.label_font = tkfont.Font(size=12)
        self.button_font = tkfont.Font(size=12, weight="bold")
        
        self.setup_ui()
        self.update_display()
        
        # Clean shutdown
        root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg="#2C3E50", padx=20, pady=20)
        main_frame.pack()
        
        # Title
        self.title_label = tk.Label(
            main_frame, 
            text="🍅 Pomodoro Timer", 
            font=self.title_font,
            fg="white",
            bg="#2C3E50"
        )
        self.title_label.pack(pady=(0, 10))
        
        # Session info
        self.session_label = tk.Label(
            main_frame,
            text="",
            font=self.label_font,
            fg="#ECF0F1",
            bg="#2C3E50"
        )
        self.session_label.pack(pady=(0, 10))
        
        # Timer display
        self.time_label = tk.Label(
            main_frame,
            text="25:00",
            font=self.time_font,
            fg="#E74C3C",
            bg="#2C3E50"
        )
        self.time_label.pack(pady=20)
        
        # Progress info
        self.progress_label = tk.Label(
            main_frame,
            text="",
            font=self.label_font,
            fg="#BDC3C7",
            bg="#2C3E50"
        )
        self.progress_label.pack(pady=(0, 20))
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg="#2C3E50")
        button_frame.pack()
        
        # Control buttons
        self.start_button = tk.Button(
            button_frame,
            text="Start",
            command=self.start_timer,
            font=self.button_font,
            bg="#27AE60",
            fg="white",
            width=8,
            relief="flat",
            cursor="hand2"
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.pause_button = tk.Button(
            button_frame,
            text="Pause",
            command=self.pause_timer,
            font=self.button_font,
            bg="#F39C12",
            fg="white",
            width=8,
            relief="flat",
            cursor="hand2",
            state=tk.DISABLED
        )
        self.pause_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            command=self.reset_timer,
            font=self.button_font,
            bg="#E74C3C",
            fg="white",
            width=8,
            relief="flat",
            cursor="hand2"
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        # Settings frame
        settings_frame = tk.Frame(main_frame, bg="#2C3E50")
        settings_frame.pack(pady=(20, 0))
        
        tk.Label(
            settings_frame,
            text="Quick Settings:",
            font=self.label_font,
            fg="#ECF0F1",
            bg="#2C3E50"
        ).pack()
        
        # Quick setting buttons
        quick_buttons_frame = tk.Frame(settings_frame, bg="#2C3E50")
        quick_buttons_frame.pack(pady=(5, 0))
        
        tk.Button(
            quick_buttons_frame,
            text="25/5 min",
            command=lambda: self.set_durations(25, 5, 15),
            font=tkfont.Font(size=10),
            bg="#34495E",
            fg="white",
            width=8,
            relief="flat",
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            quick_buttons_frame,
            text="45/10 min",
            command=lambda: self.set_durations(45, 10, 20),
            font=tkfont.Font(size=10),
            bg="#34495E",
            fg="white",
            width=8,
            relief="flat",
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            quick_buttons_frame,
            text="90/15 min",
            command=lambda: self.set_durations(90, 15, 30),
            font=tkfont.Font(size=10),
            bg="#34495E",
            fg="white",
            width=8,
            relief="flat",
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=2)
    
    def set_durations(self, work_min, short_break_min, long_break_min):
        """Set custom durations for work and break periods"""
        if self.is_running:
            messagebox.showwarning("Timer Running", "Please stop the timer before changing settings.")
            return
            
        self.work_duration = work_min * 60
        self.short_break_duration = short_break_min * 60
        self.long_break_duration = long_break_min * 60
        
        # Reset to work session with new duration
        self.reset_timer()
        messagebox.showinfo("Settings Updated", f"Timer set to {work_min}/{short_break_min} min (work/break)")
    
    def format_time(self, seconds):
        """Convert seconds to MM:SS format"""
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def update_display(self):
        """Update the timer display and session info"""
        # Update time display
        self.time_label.config(text=self.format_time(self.time_remaining))
        
        # Update session info
        if self.is_work_session:
            session_text = f"Work Session {self.current_session}"
            self.time_label.config(fg="#E74C3C")  # Red for work
            self.session_label.config(text=session_text)
        else:
            if self.current_session % self.sessions_until_long_break == 0:
                session_text = "Long Break"
                self.time_label.config(fg="#3498DB")  # Blue for long break
            else:
                session_text = "Short Break"
                self.time_label.config(fg="#2ECC71")  # Green for short break
            self.session_label.config(text=session_text)
        
        # Update progress info
        progress_text = f"Sessions completed: {max(0, self.current_session - 1)}"
        self.progress_label.config(text=progress_text)
    
    def start_timer(self):
        """Start the timer"""
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            
            # Start timer thread
            self.stop_timer_event.clear()
            self.timer_thread = threading.Thread(target=self._timer_loop, daemon=True)
            self.timer_thread.start()
    
    def pause_timer(self):
        """Pause/resume the timer"""
        if self.is_running:
            self.is_running = False
            self.stop_timer_event.set()
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
    
    def reset_timer(self):
        """Reset the timer to the beginning of current session type"""
        self.pause_timer()
        
        if self.is_work_session:
            self.time_remaining = self.work_duration
        else:
            # Determine if it should be a long break
            if self.current_session % self.sessions_until_long_break == 0:
                self.time_remaining = self.long_break_duration
            else:
                self.time_remaining = self.short_break_duration
        
        self.update_display()
    
    def _timer_loop(self):
        """Main timer loop running in separate thread"""
        while self.time_remaining > 0 and not self.stop_timer_event.is_set():
            threading.Event().wait(1)  # Wait 1 second
            if not self.stop_timer_event.is_set():
                self.time_remaining -= 1
                # Update display in main thread
                self.root.after(0, self.update_display)
        
        if self.time_remaining <= 0 and not self.stop_timer_event.is_set():
            # Timer finished
            self.root.after(0, self._timer_finished)
    
    def _timer_finished(self):
        """Called when timer reaches zero"""
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        
        # Play sound notification
        self._play_notification_sound()
        
        # Show completion message
        if self.is_work_session:
            message = f"Work session {self.current_session} completed!\nTime for a break."
            title = "Work Session Complete"
        else:
            message = "Break time is over!\nReady for the next work session?"
            title = "Break Complete"
        
        messagebox.showinfo(title, message)
        
        # Switch to next session
        if self.is_work_session:
            # Work session finished, start break
            self.is_work_session = False
            if self.current_session % self.sessions_until_long_break == 0:
                self.time_remaining = self.long_break_duration
            else:
                self.time_remaining = self.short_break_duration
        else:
            # Break finished, start next work session
            self.is_work_session = True
            self.current_session += 1
            self.time_remaining = self.work_duration
        
        self.update_display()
    
    def _play_notification_sound(self):
        """Play a notification sound when timer finishes"""
        try:
            if winsound and sys.platform.startswith('win'):
                # Play system sound on Windows
                winsound.MessageBeep(winsound.MB_ICONASTERISK)
            else:
                # Fallback: print to console
                print("\a")  # ASCII bell character
                print("🍅 Timer finished!")
        except Exception:
            print("🍅 Timer finished!")
    
    def on_close(self):
        """Clean shutdown"""
        self.stop_timer_event.set()
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.join(timeout=1)
        self.root.destroy()


def main():
    root = tk.Tk()
    app = PomodoroTimer(root)
    
    # Center the window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    
    root.mainloop()


if __name__ == "__main__":
    main()