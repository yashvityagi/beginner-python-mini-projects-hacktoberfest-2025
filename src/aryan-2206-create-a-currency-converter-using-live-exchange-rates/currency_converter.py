import requests

def get_supported_currencies():
    
    #Fetch supported currencies from Frankfurter API
    
    url = "https://api.frankfurter.app/currencies"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        print("Error: Could not fetch supported currencies.")
        return {}

def get_exchange_rate(base_currency, target_currency):
    #Fetches live exchange rate from Frankfurter API
    
    url = f"https://api.frankfurter.app/latest?from={base_currency}&to={target_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates'][target_currency]
    except requests.RequestException:
        raise Exception("Failed to fetch exchange rates.")
    except KeyError:
        raise Exception(f"Exchange rate for {target_currency} not available.")

def convert_currency(amount, rate):
    
    #Converts amount using the given exchange rate
    
    return amount * rate

def main():
    print("Currency Converter Using Frankfurter API\n")

    currencies = get_supported_currencies()
    if not currencies:
        return

    print("Supported Currencies:", ", ".join(currencies.keys()), "\n")

    while True:
        base_currency = input("Enter base currency (e.g., USD): ").upper()
        if base_currency not in currencies:
            print("Invalid currency code. Try again.\n")
            continue

        target_currency = input("Enter target currency (e.g., EUR): ").upper()
        if target_currency not in currencies:
            print("Invalid currency code. Try again.\n")
            continue

        try:
            amount = float(input(f"Enter amount in {base_currency}: "))
        except ValueError:
            print("Invalid amount. Please enter a number.\n")
            continue

        try:
            rate = get_exchange_rate(base_currency, target_currency)
            converted_amount = convert_currency(amount, rate)
            print(f"\n{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}\n")
        except Exception as e:
            print(f"Error: {e}\n")

        again = input("Do you want to convert another amount? (y/n): ").lower()
        if again != 'y':
            print("\nThank you for using the Currency Converter! 🚀")
            break

if __name__ == "__main__":
    main()
