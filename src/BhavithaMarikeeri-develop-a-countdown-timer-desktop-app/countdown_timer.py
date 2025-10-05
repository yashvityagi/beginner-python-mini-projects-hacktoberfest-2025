import tkinter as tk
from tkinter import messagebox
import time


class CountdownTimer:
    """A simple countdown timer desktop application using Tkinter."""
    
    def __init__(self, root):
        """Initialize the countdown timer application.
        
        Args:
            root: The main Tkinter window
        """
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C3E50")
        
        # Timer variables
        self.is_running = False
        self.time_left = 0
        self.total_seconds = 0
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        """Create and place all UI elements."""
        # Title Label
        title_label = tk.Label(
            self.root,
            text="⏱️ Countdown Timer",
            font=("Arial", 20, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        title_label.pack(pady=20)
        
        # Time input frame
        input_frame = tk.Frame(self.root, bg="#2C3E50")
        input_frame.pack(pady=10)
        
        # Hours input
        tk.Label(
            input_frame,
            text="Hours:",
            font=("Arial", 12),
            bg="#2C3E50",
            fg="#ECF0F1"
        ).grid(row=0, column=0, padx=5)
        
        self.hours_entry = tk.Entry(input_frame, width=5, font=("Arial", 14))
        self.hours_entry.insert(0, "0")
        self.hours_entry.grid(row=0, column=1, padx=5)
        
        # Minutes input
        tk.Label(
            input_frame,
            text="Minutes:",
            font=("Arial", 12),
            bg="#2C3E50",
            fg="#ECF0F1"
        ).grid(row=0, column=2, padx=5)
        
        self.minutes_entry = tk.Entry(input_frame, width=5, font=("Arial", 14))
        self.minutes_entry.insert(0, "0")
        self.minutes_entry.grid(row=0, column=3, padx=5)
        
        # Seconds input
        tk.Label(
            input_frame,
            text="Seconds:",
            font=("Arial", 12),
            bg="#2C3E50",
            fg="#ECF0F1"
        ).grid(row=0, column=4, padx=5)
        
        self.seconds_entry = tk.Entry(input_frame, width=5, font=("Arial", 14))
        self.seconds_entry.insert(0, "0")
        self.seconds_entry.grid(row=0, column=5, padx=5)
        
        # Timer display
        self.timer_label = tk.Label(
            self.root,
            text="00:00:00",
            font=("Arial", 36, "bold"),
            bg="#2C3E50",
            fg="#3498DB"
        )
        self.timer_label.pack(pady=20)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg="#2C3E50")
        button_frame.pack(pady=20)
        
        # Start button
        self.start_button = tk.Button(
            button_frame,
            text="Start",
            font=("Arial", 12, "bold"),
            bg="#27AE60",
            fg="white",
            width=10,
            command=self.start_timer,
            cursor="hand2"
        )
        self.start_button.grid(row=0, column=0, padx=10)
        
        # Pause button
        self.pause_button = tk.Button(
            button_frame,
            text="Pause",
            font=("Arial", 12, "bold"),
            bg="#F39C12",
            fg="white",
            width=10,
            command=self.pause_timer,
            cursor="hand2",
            state="disabled"
        )
        self.pause_button.grid(row=0, column=1, padx=10)
        
        # Reset button
        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            font=("Arial", 12, "bold"),
            bg="#E74C3C",
            fg="white",
            width=10,
            command=self.reset_timer,
            cursor="hand2"
        )
        self.reset_button.grid(row=0, column=2, padx=10)
        
    def start_timer(self):
        """Start or resume the countdown timer."""
        if not self.is_running:
            if self.time_left == 0:
                # Get time from input fields
                try:
                    hours = int(self.hours_entry.get())
                    minutes = int(self.minutes_entry.get())
                    seconds = int(self.seconds_entry.get())
                    
                    # Validate input
                    if hours < 0 or minutes < 0 or seconds < 0:
                        messagebox.showerror("Invalid Input", "Please enter positive numbers!")
                        return
                    
                    if minutes > 59 or seconds > 59:
                        messagebox.showerror("Invalid Input", "Minutes and seconds must be less than 60!")
                        return
                    
                    # Calculate total seconds
                    self.total_seconds = hours * 3600 + minutes * 60 + seconds
                    
                    if self.total_seconds == 0:
                        messagebox.showwarning("No Time Set", "Please enter a time greater than 0!")
                        return
                    
                    self.time_left = self.total_seconds
                    
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers!")
                    return
            
            # Disable input fields and start button
            self.hours_entry.config(state="disabled")
            self.minutes_entry.config(state="disabled")
            self.seconds_entry.config(state="disabled")
            self.start_button.config(state="disabled")
            self.pause_button.config(state="normal")
            
            self.is_running = True
            self.countdown()
    
    def countdown(self):
        """Update the timer display and handle countdown logic."""
        if self.is_running and self.time_left > 0:
            # Calculate hours, minutes, seconds
            hours = self.time_left // 3600
            minutes = (self.time_left % 3600) // 60
            seconds = self.time_left % 60
            
            # Update display
            time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=time_string)
            
            # Decrease time
            self.time_left -= 1
            
            # Schedule next update
            self.root.after(1000, self.countdown)
        
        elif self.is_running and self.time_left == 0:
            # Timer finished
            self.timer_label.config(text="00:00:00", fg="#E74C3C")
            self.is_running = False
            messagebox.showinfo("Time's Up!", "⏰ Countdown finished!")
            self.reset_timer()
    
    def pause_timer(self):
        """Pause the countdown timer."""
        self.is_running = False
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")
    
    def reset_timer(self):
        """Reset the countdown timer to initial state."""
        self.is_running = False
        self.time_left = 0
        self.total_seconds = 0
        self.timer_label.config(text="00:00:00", fg="#3498DB")
        
        # Re-enable input fields
        self.hours_entry.config(state="normal")
        self.minutes_entry.config(state="normal")
        self.seconds_entry.config(state="normal")
        
        # Clear input fields
        self.hours_entry.delete(0, tk.END)
        self.hours_entry.insert(0, "0")
        self.minutes_entry.delete(0, tk.END)
        self.minutes_entry.insert(0, "0")
        self.seconds_entry.delete(0, tk.END)
        self.seconds_entry.insert(0, "0")
        
        # Reset buttons
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")


def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()


if __name__ == "__main__":
    main()