# Simple Alarm Clock (Tkinter)

Beginner-friendly desktop alarm clock built with Python's standard library Tkinter.

Features
- Set an alarm using hour, minute and second (24-hour format).
- Optional: choose a WAV file to play when the alarm rings (Windows only recommended).
- Uses only standard library modules; no heavy frameworks.

Files
- `alarm.py` — main Python script (GUI and alarm logic).
- `requirements.txt` — libraries used (empty, standard library only).

How to run

1. Make sure you have Python 3.8+ installed.
2. (Optional) Create and activate a virtual environment.
3. From this folder run:

```bash
python alarm.py
```

Notes
- On Windows the app will try to use `winsound` to play beeps or WAV files. On other
  platforms it uses a simple text fallback (prints "ALARM!" to the console).
- Keep the app window open for the alarm to trigger.

Screenshot / Output sample

When the alarm rings, a dialog "Time's up!" appears and the app plays a beep (Windows) or
prints a message in the console on other platforms.

License

This project is original and free to use. Feel free to modify and improve it for learning purposes.
