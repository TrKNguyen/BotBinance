import requests
from binance.client import Client
import time
from datetime import datetime, timezone, timedelta
import pytz
import winsound
api_key=                                                                                                                                                                                            "aKhvIUWQFR0Db887GTgqD5TciZsGCKnIn5wxXiLRGNqvl6KjY0lsMAhK1gLkm4dt"
api_secret=                                                                                                                                                                                         "5Ko4ewxjOZiM5nvBZG2l3eWEn5LrrdhtfwLqnSICKyOyE8gOSvFCnWXuXJlBIbAT"
# list of OHLCV values (Open time, Open, High, Low, Close, Volume, Close time,
# Quote asset volume, Number of trades, Taker buy base asset volume, Taker buy quote asset volume, Ignore)
client = Client(api_key, api_secret)

exchange_info = client.futures_exchange_info()

coins = [symbol['symbol'] for symbol in exchange_info['symbols'] if symbol['status'] == 'TRADING']
# Define the base URL
base_url = "https://www.binance.com/futures/data/topLongShortAccountRatio"



for coin in coins:
    url = base_url + f"?symbol={coin}&period=15m&limit=1"
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse the response as JSON
        # You can now work with the data for each set of parameters
        longrate = float(data[0]["longAccount"]) * 100.0; 
        shortrate = float(data[0]["shortAccount"]) * 100;
        if (shortrate > 60):
            print(data[0]["symbol"], longrate, shortrate)



