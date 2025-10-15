# Alarm Clock Desktop App (Terminal)

Simple terminal-based alarm clock implemented in Python without external libraries.

## Features
- Set alarm by absolute time (HH:MM or HH:MM:SS, 24-hour)
- Set alarm as a relative offset in minutes (e.g. `+10` for 10 minutes from now)
- Interactive prompt when run without arguments
- Live countdown display
- Terminal bell (\a) and repeated textual alert when the alarm fires

## Files
- `alarm.py` — main alarm script (no external libraries)

## Usage
Run interactively:

```bash
python3 alarm.py
```

Set an absolute time (today or tomorrow if time already passed):

```bash
python3 alarm.py 07:30
```

Set a relative timer (minutes from now):

```bash
python3 alarm.py +10
```

Cancel countdown with Ctrl+C.

Notes:
- The script uses the ASCII bell (\a). Some terminals may mute the bell; you'll still see the text alert.
- This project intentionally avoids external dependencies so it's easy to run.

## License
This project follows the repository license.
