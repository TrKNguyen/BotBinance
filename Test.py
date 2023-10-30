import requests

symbol = 'BTCUSDT'
url = f"https://fapi.binance.com/fapi/v1/ticker/price?symbol={symbol}"
response = requests.get(url)
data = response.json()

futures_price = data['price']
print(f"The current futures price for {symbol} is {futures_price}")