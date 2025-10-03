import converter

def main():
    while True:
        print("\nUnit Converter")
        print("1. Length")
        print("2. Mass")
        print("3. Temperature")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            print("Available length units:", list(converter.length_units.keys()))
            from_unit = input("From unit: ").strip().lower()
            to_unit = input("To unit: ").strip().lower()
            try:
                value = float(input("Value: "))
                result = converter.convert_length(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result:.4f} {to_unit}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            print("Available mass units:", list(converter.mass_units.keys()))
            from_unit = input("From unit: ").strip().lower()
            to_unit = input("To unit: ").strip().lower()
            try:
                value = float(input("Value: "))
                result = converter.convert_mass(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result:.4f} {to_unit}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            print("Available temperature units:", converter.temp_units)
            from_unit = input("From unit: ").strip().lower()
            to_unit = input("To unit: ").strip().lower()
            try:
                value = float(input("Value: "))
                result = converter.convert_temperature(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result:.4f} {to_unit}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()