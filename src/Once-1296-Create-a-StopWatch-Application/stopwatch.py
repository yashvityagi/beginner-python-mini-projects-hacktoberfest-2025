import tkinter as tk
import time

# Global variables
is_running = False
passed_time = 0.0
origin_time = 0.0

def on_button_click():
    """Start or stop the stopwatch"""
    global is_running, origin_time
    if not is_running:
        origin_time = time.time()
    is_running = not is_running

def on_button_reset():
    """Reset the stopwatch"""
    global is_running, passed_time
    is_running = False
    passed_time = 0.0
    label.config(text="00:00:00.00")

def frame_update():
    """Update the displayed time every 10ms"""
    global passed_time, origin_time, is_running
    if is_running:
        current_time = time.time()
        elapsed = current_time - origin_time
        origin_time = current_time
        passed_time += elapsed

        mins, secs = divmod(passed_time, 60)
        hours, mins = divmod(mins, 60)
        label.config(text=f"{int(hours):02}:{int(mins):02}:{secs:05.2f}")
    window.after(10, frame_update)  # Update every 10 milliseconds

# Create main window
window = tk.Tk()
window.title("Stopwatch")
window.geometry("280x160")
window.resizable(False, False)

# Stopwatch label
label = tk.Label(window, text="00:00:00.00", font=("Helvetica", 36))
label.pack(pady=10)

# Buttons
start_stop_button = tk.Button(window, text="Start / Stop", width=15, command=on_button_click)
start_stop_button.pack(pady=5)

reset_button = tk.Button(window, text="Reset", width=15, command=on_button_reset)
reset_button.pack(pady=5)

# Start the frame update loop
frame_update()

# Run the app
window.mainloop()
