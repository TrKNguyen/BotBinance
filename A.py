from binance.client import Client
import time
from datetime import datetime, timezone, timedelta
import pytz
import winsound
api_key=                                                                                                                                                                                            "aKhvIUWQFR0Db887GTgqD5TciZsGCKnIn5wxXiLRGNqvl6KjY0lsMAhK1gLkm4dt"
api_secret=                                                                                                                                                                                         "5Ko4ewxjOZiM5nvBZG2l3eWEn5LrrdhtfwLqnSICKyOyE8gOSvFCnWXuXJlBIbAT"

client = Client(api_key, api_secret)
exchange_info = client.futures_exchange_info()

coins = [symbol['symbol'] for symbol in exchange_info['symbols']]
print(len(coins))
#alo alo
while(True):
    mx = 0
    coinmx = ""
    utc_now = (datetime.utcnow()- timedelta(seconds=310)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + 'Z'
    for coin in coins:  
                while True:
                       try:       
                            result = client.futures_historical_klines(symbol = coin,interval ='5m',start_str=utc_now,limit = 1)
                            val =  ( (float(result[0][2])-float(result[0][3])) /float(result[0][1] )) *100
                            if mx < val and result[0][4] > result[0][1]:
                                mx = val 
                                coinmx= coin
                                print(coinmx , mx )
                                if(mx > 2 ):
                                      winsound.Beep(2000,1000)
                                if(mx > 1.5):   
                                      winsound.Beep(2000,500)
                            if val > 1.5 and coinmx != coin:
                                print(coin , val) 
                                if(val > 2 ):
                                      winsound.Beep(2000,1000)
                                if(val > 1.5):
                                      winsound.Beep(2000,500)
                            time.sleep(0.1)      
                            break 
                       except Exception as e:
                            time.sleep(30)
                            continue 

 
    
