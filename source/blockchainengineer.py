import os
import sys
import time
from pprint import *

import ccxt  # noqa: E402

from source import API_keys


root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')
import logging
logging.basicConfig(level=logging.DEBUG)


# Exchange Class
class Exchange():
    def __init__(self, exchange_id, key, secret):
        exchange_id = exchange_id
        exchange_class = getattr(ccxt, exchange_id)
        exchange = exchange_class({
                'apiKey': key,
                'secret': secret,
                'timeout': 30000,
                'enableRateLimit': True,
        })
        print(exchange_id, "API key:", "is VALID")


# Any Time Instantiation
# enter your API public/secret keys here
bitflyer = ccxt.bitflyer({
        'enableRateLimit': True,
})
bitflyer.apiKey = API_keys.bitflyer.apiKey
bitflyer.secret = API_keys.bitflyer.secret
bittrex = ccxt.bittrex({
        'enableRateLimit': True,
})
bittrex.apiKey = API_keys.bittrex.apiKey
bittrex.secret = API_keys.bittrex.secret
coinbase = ccxt.coinbase({
        'enableRateLimit': True,
})
coinbase.apiKey = API_keys.coinbase.apiKey
coinbase.secret = API_keys.coinbase.secret
gemini = ccxt.gemini({
        'enableRateLimit': True,
})
gemini.apiKey = API_keys.gemini.apiKey
gemini.secret = API_keys.gemini.secret
kraken = ccxt.kraken({
        'enableRateLimit': True,
})
kraken.apiKey = API_keys.kraken.apiKey
kraken.secret = API_keys.kraken.secret 


def run():
    list_of_symbols = ['BTC/USD']
    list_of_exchanges = [bitflyer,bittrex]
    # list_of_exchanges = ['bitflyer','bittrex','coinbase','gemini','kraken']


    print("\n\n-------------------------------------------------------------------------\n")
    print("CRYPTOCURRENCY TRADING ALGORITHM: INITALIZE")
    # time.sleep(5)

    try:
        for exchange in list_of_exchanges:
            print("\nEXCHANGE ID: ",exchange)
            print("STATUS: ",exchange.fetch_status())
            print("DEFAULT RATE LIMIT: ",exchange.rateLimit)

            symbols = list_of_symbols
            if exchange.has['fetchOHLCV']:
                for symbol in list_of_symbols:
                    time.sleep(exchange.rateLimit/1000)
                    print(symbol,exchange.fetch_ohlcv(symbol,'1d'))
            # pprint(exchange.fetch_ticker('BTC/USD'))


    except():
        print("\n \n \nATTENTION: NON-VALID CONNECTION WITH CRYPTOCURRENCY BOT\n \n \n")
        pass



def info():
    pprint(dir(ccxt.gemini()))

    # pprint(exchange.has)
    # pprint(exchange.fetch_status())
    #
    # import random
    # if (exchange.has['fetchTicker']):
    #     pprint(exchange.fetch_ticker('BTC/USD'))
    #     symbols = list(exchange.markets.keys())
    #
    # pprint(exchange.fetch_ticker(random.choice(symbols)))
# get Exchange information
    # for exchange in list_of_exchanges:
    #     pprint(exchange.has)
    # print("\n\n-------------------------------------------------------------------------\n")
    # print("\nEXCHANGE STATUS: ")

    # # Exchange('bitflyer', API_keys.bitflyer.apiKey, API_keys.bitflyer.secret)
    # Exchange('bittrex', API_keys.bittrex.apiKey, API_keys.bittrex.secret)
    # Exchange('coinbase', API_keys.coinbase.apiKey, API_keys.coinbase.secret)
    # Exchange('gemini', API_keys.gemini.apiKey, API_keys.gemini.secret)
    # Exchange('kraken', API_keys.kraken.apiKey, API_keys.kraken.secret)


def asyncio():
    import asyncio
    import ccxt.async_support as ccxt
    async def print_gemini_ethbtc_ticker():
        gemini = ccxt.gemini()
        print(await gemini.fetch_ticker('ETH/BTC'))

    asyncio.get_event_loop().run_until_complete(print_gemini_ethbtc_ticker())



# info()
run()