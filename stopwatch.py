import time

print("Simple Stopwatch")
print("Press Enter to start")
input()  # Wait for user to start

print("Stopwatch started... press Ctrl+C to stop.")

seconds = 0
minutes = 0
hours = 0

try:
    while True:
        # Print the current time
        print(f"\r{hours:02d}:{minutes:02d}:{seconds:02d}", end="")
        time.sleep(1)  # Wait 1 second
        seconds += 1

        # Adjust minutes and hours
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1

except KeyboardInterrupt:
    print("\nStopwatch stopped.")