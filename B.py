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
coinsers = ["BTCSTUSDT","TLMUSDT","SCUSDT","FTTUSDT","RENUSDT","HNTUSDT","BTSUSDT","RAYUSDT","SRMUSDT"]
for coin in coinsers:
     coins.remove(coin)

#utcnow= (datetime.utcnow()- timedelta(seconds=310)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + 'Z'
def get(coin, interval,start_str, limit  ):
    while True:
        try:       
            result = client.futures_historical_klines(symbol = coin,interval =interval,start_str=start_str,limit=limit)
            time.sleep(0.1)
            return result      
        except Exception as e:
            time.sleep(30)
            continue 
        

def chk(result,mid):
    
    for resultperday in result:
        pre = float(resultperday[2])
        pricenow = float(result[-1][4])
        endtime =datetime.fromtimestamp( float (result[-1][6]) /1000.0)
        sttime = datetime.fromtimestamp( float (resultperday[6]) /1000.0)
        duration_days = (endtime - sttime).days
        if (duration_days > mid ): 
            continue
        if pre > pricenow:
            if ((pre-pricenow)/ pricenow ) > 0.05:
                return False
        else :
            continue
    return True

def chk1(result,mid):
    
    for resultperday in result:
        pre = float(resultperday[2])
        pricenow = float(result[-1][4])
        endtime =datetime.fromtimestamp( float (result[-1][6]) /1000.0)
        sttime = datetime.fromtimestamp( float (resultperday[6]) /1000.0)
        duration_days = (endtime - sttime).days
        if (duration_days > mid ): 
            continue
        if pre < pricenow:
            if ((pricenow-pre)/ pre ) > 0.05:
                return False
        else :
            continue
    return True  
while(True):
    mx = 0
    coinmx = ""
    
    for coin in coins: 
                if (coin[-4:]!="USDT"):
                    continue 
                
                utcnow= (datetime.utcnow()- timedelta(days=360)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + 'Z'
                result = get (coin,"1d",utcnow,360)
                l = 2
                h= 360
                endtime =datetime.fromtimestamp( float (result[-1][6]) /1000.0)
                sttime = datetime.fromtimestamp( float (result[0][6]) /1000.0)
                duration_days = (endtime - sttime).days
                if (h>duration_days):
                    h = duration_days
                while l<=h:
                    mid = int((l+h)/2)  
                    if chk(result,mid)==True:
                          l=mid+1 
                    else :
                          h=mid-1
                if h > 100:
                    print(coin,h,"top")
    for coin in coins: 
                if (coin[-4:]!="USDT"):
                    continue 
                
                utcnow= (datetime.utcnow()- timedelta(days=360)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + 'Z'
                result = get (coin,"1d",utcnow,360)
                l = 2
                h= 360
                endtime =datetime.fromtimestamp( float (result[-1][6]) /1000.0)
                sttime = datetime.fromtimestamp( float (result[0][6]) /1000.0)
                duration_days = (endtime - sttime).days
                if (h>duration_days):
                    h = duration_days
                while l<=h:
                    mid = int((l+h)/2)  
                    if chk1(result,mid)==True:
                          l=mid+1 
                    else :
                          h=mid-1
                if h > 50:
                    print(coin, h, "bottom")
                

 
    
