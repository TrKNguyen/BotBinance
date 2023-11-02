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
base_url_Account = "https://www.binance.com/futures/data/topLongShortAccountRatio"
base_url_Position = "https://www.binance.com/futures/data/topLongShortPositionRatio"

mx = -1;
coinmx = "";
def get(coin):
    url_Acount = base_url_Account + f"?symbol={coin}&period=15m&limit=1"
    url_Position = base_url_Position + f"?symbol={coin}&period=15m&limit=1"
    response_Account = requests.get(url_Acount); 
    response_Position = requests.get(url_Position);
    return (response_Account, response_Position);
for coin in coins:
    response_Account, response_Position = get(coin); 
    # Check if the request was successful (status code 200)
    if response_Account.status_code == 200 and response_Position.status_code == 200:
        data1 = response_Account.json()  # Parse the response as JSON
        data2 = response_Position.json()  # Parse the response as JSON
        # You can now work with the data for each set of parameters
        longratebyAccount = float(data1[0]["longAccount"]) * 100.0; 
        longratebyPosition = float(data2[0]["longAccount"]) * 100.0;
        if (longratebyPosition * 2 - longratebyAccount > 75):
            print(coin, longratebyAccount, longratebyPosition)
        if (longratebyPosition * 2 - longratebyAccount > mx):
            mx = longratebyPosition * 2 - longratebyAccount
            coinmx = coin
print(mx, coinmx);



