import requests

class CurrencyConverter:
    def __init__(self, api_key: str):
        """
        Initialize the converter with the given API key.
        Sets the base URL for currency conversion using the ExchangeRate API.
        """
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"
    
    def convert(self, amount: float, from_currency: str, to_currency: str):
        """
        Convert a specified amount from one currency to another.

        Parameters:
        - amount: the numeric value to convert
        - from_currency: the source currency code (e.g., "USD")
        - to_currency: the target currency code (e.g., "EUR")

        Returns:
        - Converted amount in the target currency
        """
        # Construct the API endpoint using the source currency
        url = f"{self.base_url}/{from_currency}"
        
        # Make a GET request to the currency exchange API
        response = requests.get(url)
        
        # Raise an exception if the API call fails
        if response.status_code != 200:
            raise Exception("API call failed:", response.json())
        
        # Extract the conversion rates dictionary
        rates = response.json()["conversion_rates"]
        
        # Ensure the target currency exists in the response
        if to_currency not in rates:
            raise ValueError(f"{to_currency} not found in exchange rates.")
        
        # Return the converted amount
        return amount * rates[to_currency]
