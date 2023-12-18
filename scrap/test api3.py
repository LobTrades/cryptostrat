from pycoingecko import CoinGeckoAPI
from datetime import datetime
import time

# Function to convert date to Unix timestamp
def date_to_unix(date_str):
    return int(time.mktime(datetime.strptime(date_str, '%Y-%m-%d').timetuple()))

# Initialize CoinGeckoAPI
cg = CoinGeckoAPI()

# Define start and end dates for the year 2022
start_date = "2022-01-01"
end_date = "2022-12-31"

# Convert dates to Unix timestamps
start_unix = date_to_unix(start_date)
end_unix = date_to_unix(end_date)

# Fetch Ethereum price data
eth_data = cg.get_coin_market_chart_range_by_id(id='ethereum', vs_currency='usd', from_timestamp=start_unix, to_timestamp=end_unix)

# Process and print the data
for item in eth_data['prices']:
    timestamp, price = item
    date = datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')
    print(f"Date: {date}, Price: {price}")
