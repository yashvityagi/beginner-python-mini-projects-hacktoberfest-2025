import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading

def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    
    def alarm_thread():
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if current_time == alarm_time:
                messagebox.showinfo("Alarm", "⏰ Time to wake up!")
                break
            time.sleep(1)

    threading.Thread(target=alarm_thread).start()

# GUI setup
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("300x200")
root.configure(bg="#f0f4f8")

tk.Label(root, text="Set Alarm Time", font=("Helvetica", 14), bg="#f0f4f8").pack(pady=10)

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack()

hour = tk.StringVar(root)
minute = tk.StringVar(root)
second = tk.StringVar(root)

tk.Entry(frame, textvariable=hour, width=5).grid(row=0, column=0)
tk.Label(frame, text=":", bg="#f0f4f8").grid(row=0, column=1)
tk.Entry(frame, textvariable=minute, width=5).grid(row=0, column=2)
tk.Label(frame, text=":", bg="#f0f4f8").grid(row=0, column=3)
tk.Entry(frame, textvariable=second, width=5).grid(row=0, column=4)

tk.Button(root, text="Set Alarm", command=set_alarm, bg="#0077cc", fg="white").pack(pady=20)

root.mainloop()