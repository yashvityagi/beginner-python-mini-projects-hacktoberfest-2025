"""Interactive CLI for the Dice Rolling Simulator."""

from .dice import roll_multiple


def main() -> None:
    print("Dice Rolling Simulator (type 'exit' to quit)")
    try:
        while True:
            inp = input("\nEnter number of dice and sides (format: dice sides), e.g. '2 6': ").strip()
            if inp.lower() in {"exit", "quit", "q"}:
                print("Goodbye!")
                break
                
            try:
                parts = inp.split()
                if len(parts) != 2:
                    print("Please enter two numbers: number_of_dice sides_per_die")
                    continue
                    
                num = int(parts[0])
                sides = int(parts[1])
                results = roll_multiple(num, sides)
                print(f"\nResults: {results}")
                print(f"Sum: {sum(results)}")
                
            except ValueError as e:
                print(f"Error: {e}")
                
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()