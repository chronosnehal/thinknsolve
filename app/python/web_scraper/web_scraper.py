#!/usr/bin/env python3
"""
Web Scraping and API Data Fetcher - Solution Implementation

Description: Fetches cryptocurrency data from APIs and web sources with robust error handling.
"""

import requests
import time
import json
from typing import List, Dict, Optional
from datetime import datetime
import sys

class CryptoDataFetcher:
    """A robust cryptocurrency data fetcher with API and web scraping capabilities."""

    def __init__(self, timeout: int = 10, max_retries: int = 3):
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        })

    def fetch_with_retry(self, url: str, params: Optional[Dict] = None) -> Optional[requests.Response]:
        """
        Fetch URL with retry logic and exponential backoff.

        Args:
            url: URL to fetch
            params: Optional query parameters

        Returns:
            Response object or None if all retries failed
        """
        for attempt in range(self.max_retries):
            try:
                response = self.session.get(url, params=params, timeout=self.timeout)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < self.max_retries - 1:
                    print(f"Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    print(f"All {self.max_retries} attempts failed for {url}")
        return None

    def fetch_crypto_prices(self, crypto_ids: List[str]) -> Optional[Dict]:
        """
        Fetch cryptocurrency prices from CoinGecko API.

        Args:
            crypto_ids: List of cryptocurrency IDs (e.g., ['bitcoin', 'ethereum'])

        Returns:
            Dictionary with price data or None if failed
        """
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            'ids': ','.join(crypto_ids),
            'vs_currencies': 'usd',
            'include_24hr_change': 'true',
            'include_market_cap': 'true'
        }

        print(f"Fetching price data for: {', '.join(crypto_ids)}")
        response = self.fetch_with_retry(url, params)

        if response:
            try:
                data = response.json()
                if self.validate_price_data(data, crypto_ids):
                    return data
                else:
                    print("Invalid or incomplete price data received")
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON response: {e}")

        return None

    def validate_price_data(self, data: Dict, expected_ids: List[str]) -> bool:
        """
        Validate that the API response contains expected data structure.

        Args:
            data: API response data
            expected_ids: List of expected cryptocurrency IDs

        Returns:
            True if data is valid, False otherwise
        """
        if not isinstance(data, dict):
            return False

        required_fields = ['usd', 'usd_24h_change', 'usd_market_cap']

        for crypto_id in expected_ids:
            if crypto_id not in data:
                print(f"Missing data for {crypto_id}")
                return False

            crypto_data = data[crypto_id]
            for field in required_fields:
                if field not in crypto_data:
                    print(f"Missing field {field} for {crypto_id}")
                    return False

        return True

    def fetch_additional_market_data(self, crypto_symbol: str) -> Optional[Dict]:
        """
        Simulate scraping additional market data from a web source.
        In a real scenario, this would parse HTML from a financial website.

        Args:
            crypto_symbol: Cryptocurrency symbol (e.g., 'BTC', 'ETH')

        Returns:
            Dictionary with additional market data or None if failed
        """
        # For demonstration, we'll use another API endpoint instead of HTML scraping
        # In practice, you'd use BeautifulSoup to parse HTML here
        url = f"https://api.coingecko.com/api/v3/coins/{crypto_symbol.lower()}"

        response = self.fetch_with_retry(url)
        if response:
            try:
                data = response.json()
                return {
                    'name': data.get('name', 'Unknown'),
                    'symbol': data.get('symbol', '').upper(),
                    'description': data.get('description', {}).get('en', '')[:100] + '...' if data.get('description', {}).get('en') else 'No description available'
                }
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Failed to parse additional data for {crypto_symbol}: {e}")

        return None

def format_currency(amount: float) -> str:
    """Format currency amount with appropriate precision."""
    if amount >= 1:
        return f"${amount:,.2f}"
    else:
        return f"${amount:.6f}"

def format_percentage(change: float) -> str:
    """Format percentage change with color indication."""
    sign = "+" if change > 0 else ""
    return f"{sign}{change:.2f}%"

def format_market_cap(market_cap: float) -> str:
    """Format market cap in billions or millions."""
    if market_cap >= 1_000_000_000:
        return f"${market_cap / 1_000_000_000:.1f}B"
    elif market_cap >= 1_000_000:
        return f"${market_cap / 1_000_000:.1f}M"
    else:
        return f"${market_cap:,.0f}"

def display_crypto_data(price_data: Dict, crypto_mapping: Dict[str, str]):
    """
    Display formatted cryptocurrency data.

    Args:
        price_data: Price data from API
        crypto_mapping: Mapping of crypto IDs to symbols
    """
    print("\nCryptocurrency Market Data")
    print("=" * 50)

    for crypto_id, symbol in crypto_mapping.items():
        if crypto_id in price_data:
            data = price_data[crypto_id]
            price = data.get('usd', 0)
            change_24h = data.get('usd_24h_change', 0)
            market_cap = data.get('usd_market_cap', 0)

            print(f"\n{crypto_id.title()} ({symbol})")
            print(f"  Current Price: {format_currency(price)}")
            print(f"  24h Change: {format_percentage(change_24h)}")
            print(f"  Market Cap: {format_market_cap(market_cap)}")

    print(f"\nData fetched successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """Main function to demonstrate the web scraping solution."""

    # Define cryptocurrencies to fetch
    crypto_mapping = {
        'bitcoin': 'BTC',
        'ethereum': 'ETH',
        'dogecoin': 'DOGE'
    }

    # Initialize the data fetcher
    fetcher = CryptoDataFetcher(timeout=10, max_retries=3)

    try:
        # Fetch price data from API
        price_data = fetcher.fetch_crypto_prices(list(crypto_mapping.keys()))

        if price_data:
            # Display the formatted data
            display_crypto_data(price_data, crypto_mapping)

            # Demonstrate additional data fetching (optional)
            print("\nAdditional Market Information:")
            print("-" * 30)
            for crypto_id, symbol in crypto_mapping.items():
                additional_data = fetcher.fetch_additional_market_data(crypto_id)
                if additional_data:
                    print(f"{additional_data['name']} ({additional_data['symbol']}): {additional_data['description']}")
        else:
            print("Failed to fetch cryptocurrency data. Please check your internet connection and try again.")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
