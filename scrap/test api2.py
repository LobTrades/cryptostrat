import requests
import json
from datetime import datetime

# Function to convert timestamp to date
def timestamp_to_date(timestamp):
    return datetime.utcfromtimestamp(timestamp/1000).strftime('%Y-%m-%d')

# API endpoint
url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart"

# Parameters
params = {
    "vs_currency": "usd",
    "days": "365",  # Number of days in 2022 (non-leap year)
}

# Making the request
response = requests.get(url, params=params)
data = response.json()

# Extracting and formatting the price data
prices = data["prices"]
daily_prices = [(timestamp_to_date(price[0]), price[1]) for price in prices]

# Output the results (or process them as needed)
for date, price in daily_prices:
    print(f"Date: {date}, Price: {price}")
