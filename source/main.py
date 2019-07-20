# root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root + '/python')
import logging
import time
from pprint import *

import ccxt  # noqa: E402

from source import API_keys


# logging.basicConfig(level = logging.DEBUG)

# Any Time Instantiation
# enter your API public/secret keys here
bitflyer = ccxt.bitflyer({
        'enableRateLimit':True,
})
bitflyer.apiKey = API_keys.bitflyer.apiKey
bitflyer.secret = API_keys.bitflyer.secret
bittrex = ccxt.bittrex({
        'enableRateLimit':True,
})
bittrex.apiKey = API_keys.bittrex.apiKey
bittrex.secret = API_keys.bittrex.secret
coinbase = ccxt.coinbase({
        'enableRateLimit':True,
})
coinbase.apiKey = API_keys.coinbase.apiKey
coinbase.secret = API_keys.coinbase.secret
gemini = ccxt.gemini({
        'enableRateLimit':True,
})
gemini.apiKey = API_keys.gemini.apiKey
gemini.secret = API_keys.gemini.secret
kraken = ccxt.kraken({
        'enableRateLimit':True,
})
kraken.apiKey = API_keys.kraken.apiKey
kraken.secret = API_keys.kraken.secret


def info():
    pprint(dir(ccxt.gemini()))


def asyncio():
    import asyncio
    import ccxt.async_support as ccxt

    async def print_gemini_ethbtc_ticker():
        gemini = ccxt.gemini()
        print(await gemini.fetch_ticker('ETH/BTC'))

    asyncio.get_event_loop().run_until_complete(print_gemini_ethbtc_ticker())


# get a deposit address for BTC
# address = client.get_deposit_address(asset='BTC')
# list_of_exchanges = [bitflyer]
# list_of_exchanges = [bittrex]
list_of_exchanges = [bitflyer, bittrex]
all_symbols = []
my_symbols = ['BTC/USD']


def initialize():  # set initial conditions for Bot

    print("\n\n-------------------------------------------------------------------------\n")
    print("CRYPTOCURRENCY TRADING ALGORITHM: INITALIZE")

    i = 0
    try:
        for exchange in list_of_exchanges:
            print("\nEXCHANGE ID: ", exchange)
            print("STATUS: ", exchange.fetch_status())
            print("DEFAULT RATE LIMIT: ", exchange.rateLimit)
            time.sleep(3)

            list_of_symbols = []
            if i > 0:
                break

    except():
        print("\n \n \nATTENTION: NON-VALID CONNECTION WITH CRYPTOCURRENCY BOT\n \n \n")
        pass


def diversify():
    # collect all balances across exchange into wallets
    # then diversify into specific amounts
    # ex: 50% btc, 5% each of 8 next-top coins, 10x 1% of micro-caps
    for exchange in list_of_exchanges:
        print("\nExchange Balances: ")
        pprint(exchange.fetch_balance())
        time.sleep(3)
        # print(exchange.fetch_deposit_address('USD'))
        # pprint(bitflyer.load_markets())


def ActiveTrader(bidlist,asklist):
    # active trader - continuous loop of calling trader functions
        # arbitrage function
    oppo=0
    arb_list = ['BTC/USD']
    for i in range(len(list_of_exchanges)):
        orderbook=list_of_exchanges[i].fetch_order_book(symbol=arb_list[0])
        if(bidlist[i] != orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None):
            oppo=1
            # print(bidlist[i])
            # print( orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None)
        if(asklist[i] != orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None):
            oppo=1
            # print(asklist[i])
            # print(orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None)
        bidlist[i] = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
        asklist[i] = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
    if(oppo==1):
        opportunity(bidlist,asklist)
    return (bidlist,asklist)

def opportunity(bidlist,asklist):
    print('trying... commond this later')
    for i in range(len(list_of_exchanges)):
        for j in range(len(list_of_exchanges)):
            if(bidlist[j]>asklist[i]):
                print('Opportunity: buy from ',list_of_exchanges[i],' with $',asklist[i],' sale to ',list_of_exchanges[j],' with $',bidlist[j])

def arbitrage():
    print("\n\nArbitrage Function ")
    coins = ['BTC']       # coins to arbitrage
    bidlist=[]
    asklist=[]
    for exchange in list_of_exchanges:
        symbols = exchange.load_markets()
        if symbols is None:
            print("\n----------------\nNext Exchange\n----------------")
        elif len(symbols)<5:
            print("\n----------------\nMore Symbol Pairs Required\n----------------")
        else:
            print("\n----------Exchange: ", exchange.id, "----------")

        exchange_info = dir(exchange)
        # pprint(exchange_info)
        print(exchange.symbols)

        # find currency pairs to trade
        pairs = []
        for sym in symbols:
            for symbol in coins:
                if symbol in sym:
                    pairs.append(sym)
        print(pairs)
        time.sleep(3)


        # from coin 1 to coin 2 - ETH/BTC - Bid
        # from coin 2 to coin 3 - ETH/LTC - Ask
        # from coin 3 to coin 1 - BTC/LTC - Bid
        # arb_list = ['ETH/BTC','ETH/LTC','BTC/LTC']
        arb_list = ['BTC/USD']

        # determine rates for our 3 currency pairs using order book
        i = 0
        exch_rate_list = []
        for sym in arb_list:
            if sym in symbols:
                # print("\n\n")
                orderbook = exchange.fetch_order_book(symbol=sym)
                # print("\n\n")
                bitflyer.parse_order_book(orderbook=orderbook)
                # print("\n\n")
                # pprint(orderbook)
                # print("\n\n")
                # orderbook = exchange.fetch_order_book(exchange.symbols[0])
                bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
                # print("\n\n")
                ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
                # print("\n\n")
                bidlist.append(bid)
                asklist.append(ask)
                spread = (ask - bid) if (bid and ask) else None
                data = (exchange.id, 'market price', {'bid': bid, 'ask': ask, 'spread': spread})
                pprint(data)
                print("\n\n")
                # depth = exchange.fetch_order_book(symbol=sym)
                # pprint(depth)
                time.sleep(3)
                # exch_rate_list.append(depth(['bids'][0][0]))
    return (bidlist,asklist)


def run():

    # info()

    initialize()
    
    # diversify()


    (bidlist,asklist)=arbitrage()
    portfolio = 10  # BTC



    while 1:
        # active trader - 'scalping', swing trading, arbitrage
        ActiveTrader(bidlist,asklist)



run()
