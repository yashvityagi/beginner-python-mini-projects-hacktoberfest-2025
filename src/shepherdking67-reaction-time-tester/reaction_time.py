import time
import random

def reaction_time_test():
    print("🎮 Reaction Time Tester")
    print("Get ready... Wait for 'GO!' then press Enter as fast as you can.")
    print("Press Enter to start...")
    input()

    # Random delay before "GO!"
    wait_time = random.uniform(2, 5)
    print("Wait for it...")
    time.sleep(wait_time)

    print("GO! 🚦")
    start_time = time.time()

    input()  # Wait for user to hit Enter
    end_time = time.time()

    reaction_time = end_time - start_time
    print(f"⚡ Your reaction time: {reaction_time:.3f} seconds")

if __name__ == "__main__":
    reaction_time_test()
