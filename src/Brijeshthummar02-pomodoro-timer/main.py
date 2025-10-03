import time

def countdown(minutes):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f'\r{timer}', end='')
        time.sleep(1)
        total_seconds -= 1
    print('\nTime\'s up!')

def main():
    cycle = 1
    while True:
        print(f"\nCycle {cycle}: Work session (25 minutes)")
        countdown(25)
        print("Break time (5 minutes)")
        countdown(5)
        cycle += 1

if __name__ == "__main__":
    main()