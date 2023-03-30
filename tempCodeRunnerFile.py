client = Client(api_key, api_secret)
exchange_info = client.futures_exchange_info()

coins = [symbol['symbol'] for symbol in exchange_info['symbols']]