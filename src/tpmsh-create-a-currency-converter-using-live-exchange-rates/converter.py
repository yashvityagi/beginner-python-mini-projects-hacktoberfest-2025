import requests

def fetch_rates(base_currency="EUR"):
    """
    Fetches live exchange rates from the Frankfurter API using the specified base currency.

    Parameters:
        base_currency (str): The currency to use as the base for conversion (default is 'EUR').

    Returns:
        dict: A dictionary containing exchange rates and metadata.

    Raises:
        Exception: If the API request fails.
    """
    url = f"https://api.frankfurter.dev/v1/latest?base={base_currency.upper()}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Unable to retrieve exchange rates. Please check your internet connection or try again later.")
    return response.json()

def convert_currency(amount, from_currency, to_currency):
    """
    Converts a given amount from one currency to another using live exchange rates.

    Parameters:
        amount (float): The amount of money to convert.
        from_currency (str): The currency code to convert from.
        to_currency (str): The currency code to convert to.

    Returns:
        None: Prints the conversion result to the console.
    """
    data = fetch_rates(base_currency=from_currency)
    rates = data.get("rates", {})
    to_currency = to_currency.upper()

    if to_currency not in rates:
        raise ValueError(f"Sorry, '{to_currency}' is not supported or unavailable at the moment.")

    rate = rates[to_currency]
    converted = amount * rate
    print(f"\nConversion Result:")
    print(f"{amount:.2f} {from_currency.upper()} = {converted:.2f} {to_currency} (Exchange Rate: {rate})")

if __name__ == "__main__":
    print("Welcome to the Live Currency Converter!")
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Convert from (e.g., USD): ").strip()
        to_currency = input("Convert to (e.g., INR): ").strip()
        convert_currency(amount, from_currency, to_currency)
    except ValueError:
        print("Invalid input. Please enter a numeric amount and valid currency codes.")
    except Exception as e:
        print("Error:", e)
