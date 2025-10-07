# Web Scraping and API Data Fetcher

## Context
In modern software development, applications frequently need to gather data from external sources like websites, APIs, and online databases. Web scraping and API integration are essential skills for data collection, competitive analysis, price monitoring, and building data-driven applications. This problem simulates a real-world scenario where you need to fetch financial data from multiple sources and process it for analysis.

## Problem Statement
Build a Python script that fetches cryptocurrency price data from a public API and scrapes additional market information from a web source. The solution should handle both JSON API responses and HTML parsing, demonstrating practical data retrieval and processing skills.

Your script should:
1. Fetch current cryptocurrency prices from a public REST API
2. Parse and extract specific data fields from the JSON response
3. Handle HTTP errors and API rate limits gracefully
4. Scrape additional market data from a secondary HTML source
5. Combine and format the data for analysis
6. Implement proper error handling and data validation

## Requirements
- Use the `requests` library for HTTP requests
- Use `BeautifulSoup` for HTML parsing when needed
- Fetch data for at least 3 different cryptocurrencies (Bitcoin, Ethereum, Dogecoin)
- Extract: symbol, current price, 24h price change, market cap
- Handle network timeouts and HTTP error codes (404, 500, etc.)
- Implement retry logic for failed requests (max 3 attempts)
- Validate that fetched data contains expected fields
- Format output as clean, readable text and structured data
- Complete execution within 10 seconds for normal operations
- Handle missing or malformed data gracefully

## Assumptions
- Internet connection is available
- Public APIs are accessible (no authentication required)
- API responses are in JSON format
- HTML structure is relatively stable for scraping
- Rate limits allow for reasonable request frequency
- Python 3.7+ environment with requests and beautifulsoup4 available

## For Examiner

### Difficulty Level
Intermediate

### Expected Time
**MANDATORY**: 30-40 minutes

### Key Concepts Being Tested
- HTTP requests and API integration
- JSON data parsing and manipulation
- HTML parsing with BeautifulSoup
- Error handling and exception management
- Data validation and type checking
- Retry mechanisms and timeout handling
- Clean code structure and documentation
- Practical web scraping techniques

### Hints (if needed)
- Use CoinGecko API (free, no auth required): `https://api.coingecko.com/api/v3/simple/price`
- Consider using sessions for connection pooling
- Implement exponential backoff for retries
- Use CSS selectors or XPath for HTML parsing
- Test with invalid URLs to verify error handling

### Solution Approach Plan
1. Set up HTTP session with proper headers and timeouts
2. Create functions for API requests with retry logic
3. Implement JSON response parsing and validation
4. Add HTML scraping functionality for additional data
5. Create data combination and formatting logic
6. Add comprehensive error handling
7. Test with various scenarios (success, failure, timeout)

## Example Input/Output
```
Input: ["bitcoin", "ethereum", "dogecoin"]
Output: 
Cryptocurrency Market Data
==========================
Bitcoin (BTC)
  Current Price: $43,250.50
  24h Change: +2.45%
  Market Cap: $847.2B

Ethereum (ETH)
  Current Price: $2,650.75
  24h Change: -1.23%
  Market Cap: $318.7B

Dogecoin (DOGE)
  Current Price: $0.087
  24h Change: +5.67%
  Market Cap: $12.4B

Data fetched successfully at 2025-10-07 14:30:15
```
