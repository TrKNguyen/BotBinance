from binance.client import Client
import time
from datetime import datetime, timezone, timedelta
import pytz
import winsound
import random
from binance.enums import HistoricalKlinesType
from dateutil import tz
api_key =                                                                                                                                                                                                                               "aKhvIUWQFR0Db887GTgqD5TciZsGCKnIn5wxXiLRGNqvl6KjY0lsMAhK1gLkm4dt"
api_secret =                                                                                                                                                                                                                            "5Ko4ewxjOZiM5nvBZG2l3eWEn5LrrdhtfwLqnSICKyOyE8gOSvFCnWXuXJlBIbAT"

client = Client(api_key, api_secret)
exchange_info = client.futures_exchange_info()
exchange_info_spot = client.get_exchange_info()

coins = [symbol['symbol'] for symbol in exchange_info['symbols'] if symbol['status'] == 'TRADING']
coinspot = [symbol['symbol'] for symbol in exchange_info_spot['symbols'] if symbol['status'] == 'TRADING']

coiners = ["DEFIUSDT","XRMUSDT","SRMUSDT",'HNTUSDT', 'CVCUSDT', 'BTCSTUSDT', 'FTTUSDT',"BTCSTUSDT","TLMUSDT","SCUSDT","FTTUSDT","RENUSDT","HNTUSDT","BTSUSDT","RAYUSDT","SRMUSDT","CVCUSDT"]
for coin in coins:
    if coin not in coinspot:
        coiners.append(coin)
    if coin[-4:]!="USDT":
        coiners.append(coin)
for coin in coiners:
    if coin in coins:
        coins.remove(coin)
random.shuffle(coins)
print(len(coins))
#print(len(coins))
# alo alo
# list of OHLCV values (Open time, Open, High, Low, Close, Volume, Close time,
# Quote asset volume, Number of trades, Taker buy base asset volume, Taker buy quote asset volume, Ignore)

while (True):
    mx = 0
    coinmx = ""
    utc_now = (datetime.utcnow() - timedelta(seconds=310)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + 'Z'
    coinmx = ""
    valmx = -1
    list = []
    for coin in coins:

        while True:
            try:

                resultspot = client.get_historical_klines(symbol=coin, interval='5m', start_str=utc_now, limit=1,
                klines_type  = HistoricalKlinesType.SPOT)
                resultfutures = client.futures_historical_klines(symbol=coin, interval='5m', start_str=utc_now, limit=1)
                #print(len(resultfutures),len(resultspot))
                val = (float(resultspot[-1][4])-float(resultfutures[-1][4]))/float(resultspot[-1][4]) *100
                if(val>valmx):
                    valmx = val
                    coinmx = str(coin)
                if(val>1):
                    print(coin,val)
                if (val > 2):
                    winsound.Beep(2000,2000)
                break
            except Exception as e:
                #print(e)
                print(coin)
                #time.sleep(10)
                break
    print(coinmx, valmx)
