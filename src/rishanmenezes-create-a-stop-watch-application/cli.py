"""Command line interface for the stopwatch."""

import sys
import time
import select
from typing import NoReturn

from .stopwatch import Stopwatch


def format_time(seconds: float) -> str:
    """Format time in seconds to HH:MM:SS.ss format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:05.2f}"


def print_instructions() -> None:
    """Print usage instructions."""
    print("\nStopwatch Controls:")
    print("SPACE - Start/Stop")
    print("L - Record Lap")
    print("R - Reset")
    print("Q - Quit")
    print("\nCurrent time will update every 0.1 seconds.")


def main() -> NoReturn:
    """Run the stopwatch CLI application."""
    stopwatch = Stopwatch()
    print_instructions()

    try:
        while True:
            # Clear the last line to update the time
            if stopwatch.is_running:
                sys.stdout.write("\033[F")  # Move cursor up one line
                sys.stdout.write("\033[K")  # Clear line
                elapsed = format_time(stopwatch.elapsed)
                print(f"\rElapsed Time: {elapsed}", end="")
                time.sleep(0.1)  # Update every 0.1 seconds

            # Check for keyboard input (non-blocking)
            if sys.stdin.isatty() and sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                char = sys.stdin.read(1).upper()

                if char == ' ':  # Space
                    if stopwatch.is_running:
                        stopwatch.stop()
                        print("\nStopped!")
                    else:
                        stopwatch.start()
                        print("\nStarted!")

                elif char == 'L':  # Lap
                    lap_time = stopwatch.lap()
                    if lap_time is not None:
                        lap_num = len(stopwatch.laps)
                        print(f"\nLap {lap_num}: {format_time(lap_time)}")

                elif char == 'R':  # Reset
                    stopwatch.reset()
                    print("\nReset!")
                    print_instructions()

                elif char == 'Q':  # Quit
                    print("\nQuitting...")
                    sys.exit(0)

    except KeyboardInterrupt:
        print("\nQuitting...")
        sys.exit(0)


if __name__ == "__main__":
    main()