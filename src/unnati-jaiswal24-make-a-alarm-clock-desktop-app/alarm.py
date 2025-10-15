#!/usr/bin/env python3
"""
Simple terminal Alarm Clock (no external libraries).
Features:
- Set alarm by absolute time (HH:MM) or relative minutes (e.g. +15)
- Shows countdown every second
- Uses system beep and repeated text alert when time reaches
- Works on macOS/Linux/Windows terminals without extra packages

Usage:
  python alarm.py       # interactive prompts
  python alarm.py 07:30 # set to today at 07:30
  python alarm.py +10   # set alarm 10 minutes from now

"""
from __future__ import annotations

import sys
import time
from datetime import datetime, timedelta


def parse_arg(arg: str) -> datetime:
    now = datetime.now()
    arg = arg.strip()
    if not arg:
        raise ValueError("Empty argument")
    # Relative minutes: +N or -N
    if arg.startswith(('+', '-')) and arg[1:].isdigit():
        minutes = int(arg)
        return now + timedelta(minutes=minutes)
    # Absolute time HH:MM (24-hour) maybe with optional :SS
    parts = arg.split(":")
    if len(parts) >= 2 and all(p.isdigit() for p in parts[:2]):
        hour = int(parts[0])
        minute = int(parts[1])
        sec = int(parts[2]) if len(parts) >= 3 and parts[2].isdigit() else 0
        target = now.replace(hour=hour, minute=minute, second=sec, microsecond=0)
        # If the time already passed today, schedule for tomorrow
        if target <= now:
            target += timedelta(days=1)
        return target
    raise ValueError("Invalid time format. Use HH:MM or +N minutes")


def prompt_user() -> datetime:
    print("Simple Alarm Clock (no external libs)")
    print("Enter alarm time as HH:MM (24-hour) or as +N for minutes from now.")
    while True:
        s = input("Alarm time: ").strip()
        try:
            return parse_arg(s)
        except Exception as e:
            print(f"Error: {e}")


def readable_delta(td: timedelta) -> str:
    total = int(td.total_seconds())
    if total < 0:
        total = 0
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def beep():
    # Try multiple ways to produce a beep across platforms
    try:
        # ASCII bell
        sys.stdout.write('\a')
        sys.stdout.flush()
    except Exception:
        pass


def run_alarm(target: datetime):
    print(f"Alarm set for {target.strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        while True:
            now = datetime.now()
            delta = target - now
            total = int(delta.total_seconds())
            if total <= 0:
                break
            # Update once per second
            sys.stdout.write(f"\rTime left: {readable_delta(delta)} ")
            sys.stdout.flush()
            # Sleep up to 1 second, but handle KeyboardInterrupt quickly
            for _ in range(10):
                time.sleep(0.1)
                if datetime.now() >= target:
                    break
        # When reached
        print('\nTime is up!')
        # Repeat audible/visual alert for ~15 seconds
        end = time.time() + 15
        while time.time() < end:
            beep()
            print('*** ALARM ***\r', end='')
            sys.stdout.flush()
            time.sleep(0.6)
        print('\nAlarm finished.')
    except KeyboardInterrupt:
        print('\nAlarm cancelled by user.')


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    try:
        if len(argv) >= 1:
            target = parse_arg(argv[0])
        else:
            target = prompt_user()
    except Exception as e:
        print(f"Error parsing time: {e}")
        return 2
    run_alarm(target)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
