"""
Simple Alarm Clock Desktop App (Tkinter)

Beginner-friendly alarm app that lets the user set a time (24-hour) and plays a beep
when the alarm time is reached. Uses only Python standard library (tkinter, datetime,
and winsound on Windows).

How it works:
- User selects hour, minute, second using Spinbox widgets.
- Click "Set Alarm" to schedule the alarm for the next occurrence of that time.
- When time is reached a dialog appears and the app plays a repeating beep until
  the user clicks "Stop Alarm".

This file is intentionally self-contained and easy to read for beginners.
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import tkinter.font as tkfont
import datetime
import time
import threading
import sys

try:
    import winsound
except Exception:
    winsound = None

# Try to import pygame for MP3/WAV playback and stopping support
try:
    import pygame
    pygame_available = True
except Exception:
    pygame = None
    pygame_available = False


class AlarmApp:
    def __init__(self, root):
        self.root = root
        root.title("Simple Alarm Clock")
        root.resizable(False, False)

        # fonts
        self.title_font = tkfont.Font(size=14, weight="bold")
        self.label_font = tkfont.Font(size=11)
        self.btn_font = tkfont.Font(size=11)

        # Frame for time selection
        frm = tk.Frame(root, padx=16, pady=12)
        frm.pack()

        tk.Label(frm, text="Set alarm (24-hour)", font=self.title_font).grid(row=0, column=0, columnspan=6, pady=(0, 8))

        tk.Label(frm, text="Hour", font=self.label_font).grid(row=1, column=0)
        tk.Label(frm, text="Min", font=self.label_font).grid(row=1, column=2)
        tk.Label(frm, text="Sec", font=self.label_font).grid(row=1, column=4)

        self.hour_var = tk.StringVar(value=datetime.datetime.now().strftime("%H"))
        self.min_var = tk.StringVar(value=datetime.datetime.now().strftime("%M"))
        self.sec_var = tk.StringVar(value=datetime.datetime.now().strftime("%S"))

        self.hour_sb = tk.Spinbox(frm, from_=0, to=23, wrap=True, width=4, textvariable=self.hour_var, format="%02.0f", font=self.label_font)
        self.hour_sb.grid(row=2, column=0, padx=(0, 4))

        tk.Label(frm, text=":", font=self.label_font).grid(row=2, column=1)

        self.min_sb = tk.Spinbox(frm, from_=0, to=59, wrap=True, width=4, textvariable=self.min_var, format="%02.0f", font=self.label_font)
        self.min_sb.grid(row=2, column=2, padx=(4, 4))

        tk.Label(frm, text=":", font=self.label_font).grid(row=2, column=3)

        self.sec_sb = tk.Spinbox(frm, from_=0, to=59, wrap=True, width=4, textvariable=self.sec_var, format="%02.0f", font=self.label_font)
        self.sec_sb.grid(row=2, column=4, padx=(4, 0))

        # Buttons
        self.set_btn = tk.Button(frm, text="Set Alarm", command=self.set_alarm, width=12, font=self.btn_font, bg="#4CAF50", fg="white")
        self.set_btn.grid(row=3, column=0, columnspan=2, pady=(12, 0), padx=4)

        self.stop_btn = tk.Button(frm, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED, width=12, font=self.btn_font, bg="#F44336", fg="white")
        self.stop_btn.grid(row=3, column=2, columnspan=2, pady=(12, 0), padx=4)

        self.choose_sound_btn = tk.Button(frm, text="Choose Sound (MP3/WAV)", command=self.choose_sound, width=28, font=self.btn_font)
        self.choose_sound_btn.grid(row=4, column=0, columnspan=6, pady=(12, 0))

        # Status label
        self.status_var = tk.StringVar(value="No alarm set")
        tk.Label(root, textvariable=self.status_var, pady=8, font=self.label_font).pack()

        # current time display
        self.time_var = tk.StringVar(value="")
        self.time_label = tk.Label(root, textvariable=self.time_var, font=tkfont.Font(size=12, weight="bold"))
        self.time_label.pack()

        # Internal state
        self.alarm_time = None
        self.sound_path = None
        self._stop_sound_event = threading.Event()
        self._sound_thread = None

        # Start the periodic checker
        self._checker_running = True
        self.root.after(200, self.check_alarm)
        self._update_clock()

        # Clean shutdown
        root.protocol("WM_DELETE_WINDOW", self.on_close)

    def choose_sound(self):
        # Allow user to pick a WAV file (winsound supports WAV). If not on Windows, file selection still allowed
        p = filedialog.askopenfilename(title="Choose MP3 or WAV file (optional)", filetypes=[("Audio files", "*.mp3;*.wav"), ("All files", "*")])
        if p:
            self.sound_path = p
            self.status_var.set(f"Sound selected: {p}")

    def set_alarm(self):
        try:
            h = int(self.hour_var.get())
            m = int(self.min_var.get())
            s = int(self.sec_var.get())
            if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
                raise ValueError
        except Exception:
            messagebox.showerror("Invalid time", "Please enter valid hour/min/sec values.")
            return

        now = datetime.datetime.now()
        target = now.replace(hour=h, minute=m, second=s, microsecond=0)
        if target <= now:
            # schedule for next day
            target += datetime.timedelta(days=1)

        self.alarm_time = target
        self.status_var.set(f"Alarm set for {self.alarm_time.strftime('%Y-%m-%d %H:%M:%S')}")
        self.set_btn.config(state=tk.DISABLED)

    def stop_alarm(self):
        # Stop any playing sound and clear alarm
        self._stop_sound_event.set()
        # Stop pygame music if used
        try:
            if pygame_available and pygame and pygame.mixer.get_init():
                pygame.mixer.music.stop()
        except Exception:
            pass

        if self._sound_thread and self._sound_thread.is_alive():
            self._sound_thread.join(timeout=1)

        self._stop_sound_event.clear()
        self.alarm_time = None
        self.status_var.set("No alarm set")
        self.set_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

    def _play_sound_loop(self):
        # Keep playing a short beep (or WAV if provided) until stop event set
        # If pygame is available, prefer it for MP3/WAV playback because it supports stop control
        if self.sound_path and pygame_available:
            try:
                # Initialize mixer if not already
                if not pygame.mixer.get_init():
                    pygame.mixer.init()
                pygame.mixer.music.load(self.sound_path)
                pygame.mixer.music.play(-1)  # loop indefinitely
                while not self._stop_sound_event.is_set():
                    time.sleep(0.2)
                pygame.mixer.music.stop()
                return
            except Exception:
                # fallback to other methods if pygame fails
                pass

        # If winsound available and sound_path is WAV, use it (Windows)
        if self.sound_path and winsound and self.sound_path.lower().endswith('.wav') and sys.platform.startswith('win'):
            while not self._stop_sound_event.is_set():
                winsound.PlaySound(self.sound_path, winsound.SND_FILENAME)
                time.sleep(0.2)
            return

        # If winsound available, beep repeatedly
        if winsound:
            while not self._stop_sound_event.is_set():
                try:
                    winsound.Beep(1000, 500)
                except RuntimeError:
                    break
                time.sleep(0.2)
            return

        # Non-Windows fallback: print alarm message repeatedly
        while not self._stop_sound_event.is_set():
            print("ALARM! (no sound available)")
            time.sleep(1)

    def trigger_alarm(self):
        # Called when time reached
        self.status_var.set("Alarm ringing!")
        self.stop_btn.config(state=tk.NORMAL)

        # Start sound thread
        self._stop_sound_event.clear()
        self._sound_thread = threading.Thread(target=self._play_sound_loop, daemon=True)
        self._sound_thread.start()

        # Show a blocking dialog in a separate small thread so the mainloop isn't frozen by any long blocking
        def popup():
            messagebox.showinfo("Alarm", "Time's up!")

        threading.Thread(target=popup, daemon=True).start()

    def check_alarm(self):
        # Periodically called via after
        if self.alarm_time:
            now = datetime.datetime.now()
            if now >= self.alarm_time:
                # trigger and clear alarm_time so it doesn't retrigger
                self.alarm_time = None
                self.trigger_alarm()

        if self._checker_running:
            self.root.after(500, self.check_alarm)

    def _update_clock(self):
        # Update the current time display every second
        now = datetime.datetime.now()
        self.time_var.set(now.strftime("%Y-%m-%d %H:%M:%S"))
        if self._checker_running:
            self.root.after(1000, self._update_clock)

    def on_close(self):
        # Clean up threads
        self._checker_running = False
        self._stop_sound_event.set()
        try:
            if self._sound_thread and self._sound_thread.is_alive():
                self._sound_thread.join(timeout=1)
        except Exception:
            pass
        try:
            if pygame_available and pygame and pygame.mixer.get_init():
                pygame.mixer.quit()
        except Exception:
            pass
        self.root.destroy()


def main():
    root = tk.Tk()
    app = AlarmApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
