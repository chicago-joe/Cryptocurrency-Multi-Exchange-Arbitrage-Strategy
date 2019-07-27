from source import API_keys
from source.init_exchanges import *
import ccxt
import time
from pprint import pprint
import numpy as np


# import os, sys
# root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root + '/python')

# import logging
# logging.basicConfig(level = logging.DEBUG)


list_of_exchanges = [bitflyer, bittrex, kraken, gemini]
trades_executed = []
trades_profit = []
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
            time.sleep(2)
            list_of_symbols = []
            if i > 0:
                break

    except():
        print("\n \n \nATTENTION: NON-VALID CONNECTION WITH CRYPTOCURRENCY BOT\n \n \n")
        pass


def ActiveTrader(bidlist, asklist):
    # active trader - continuous loop of calling trader functions
    # arbitrage function
    oppo = 0
    arb_list = ['BTC/USD']
    for i in range(len(list_of_exchanges)):
        orderbook = list_of_exchanges[i].fetch_order_book(symbol = arb_list[0])
        if (bidlist[i] != orderbook['bids'][0] if len(orderbook['bids']) > 0 else None):
            oppo = 1
            # print(bidlist[i])
            # print( orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None)
        if (asklist[i] != orderbook['asks'][0] if len(orderbook['asks']) > 0 else None):
            oppo = 1
            # print(asklist[i])
            # print(orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None)
        bidlist[i] = orderbook['bids'][0] if len(orderbook['bids']) > 0 else None
        asklist[i] = orderbook['asks'][0] if len(orderbook['asks']) > 0 else None
    if (oppo == 1):
        opportunity(bidlist, asklist)

    return (bidlist, asklist)


def opportunity(bidlist, asklist):
    print('searching for opportunities...')

    largestbid = -1
    lowestask = 999999999
    largestbidname = ''
    lowestaskname = ''
    bidvol = 0
    askvol = 0

    for i in range(len(list_of_exchanges)):
        if bidlist[i][0] > largestbid:
            largestbidname = list_of_exchanges[i]
            largestbid = bidlist[i][0]
            bidvol = bidlist[i][1]
        if asklist[i][0] < lowestask:
            lowestaskname = list_of_exchanges[i]
            lowestask = asklist[i][0]
            askvol = asklist[i][1]

    spread = largestbid - lowestask
    askcost = 0
    bidcost = 0
    if (largestbid > lowestask):

        if bidvol > askvol:
            print('Opportunity: buy from ', lowestaskname, ' with $', lowestask, ' sell to ', largestbidname, ' with $', largestbid, ' * ',
                  askvol)
            print('spread = %.5f' % spread)
            askcost += askvol * lowestask
            bidcost += askvol * largestbid
            pricediff = spread * askvol
            orderbook = lowestaskname.fetch_order_book(symbol = 'BTC/USD')
            for i in range(len(orderbook['asks'])):
                if (i != 0):
                    if largestbid > orderbook['asks'][i][0]:
                        if (askvol + orderbook['asks'][i][1] >= bidvol):
                            print('buy from ', lowestaskname, ' with $', orderbook['asks'][i][0], ' sell to ', largestbidname, ' with $',
                                  largestbid, ' * ', bidvol - askvol)
                            print('spread = %.5f' % (largestbid - orderbook['asks'][i][0]))
                            pricediff += (largestbid - orderbook['asks'][i][0]) * (bidvol - askvol)
                            askcost += (bidvol - askvol) * orderbook['asks'][i][0]
                            bidcost += (bidvol - askvol) * largestbid
                            break
                        else:
                            print('buy from ', lowestaskname, ' with $', orderbook['asks'][i][0], ' sell to ', largestbidname, ' with $',
                                  largestbid, ' * ', orderbook['asks'][i][1])
                            print('spread = %.5f' % (largestbid - orderbook['asks'][i][0]))
                            askvol += orderbook['asks'][i][1]
                            pricediff += (largestbid - orderbook['asks'][i][0]) * orderbook['asks'][i][1]
                            askcost += orderbook['asks'][i][1] * orderbook['asks'][i][0]
                            bidcost += orderbook['asks'][i][1] * largestbid
                    else:
                        break
        else:
            print('Opportunity: buy from ', lowestaskname, ' with $', lowestask, ' sell to ', largestbidname, ' with $', largestbid, ' * ',
                  bidvol)
            print('spread = %.5f' % spread)
            askcost += bidvol * lowestask
            bidcost += bidvol * largestbid
            pricediff = spread * bidvol
            orderbook = largestbidname.fetch_order_book(symbol = 'BTC/USD')

            for i in range(len(orderbook['bids'])):
                if (i != 0):
                    if orderbook['bids'][i][0] > lowestask:
                        if (bidvol + orderbook['bids'][i][1] >= askvol):
                            print('buy from ', lowestaskname, ' with $', lowestask, ' sell to ', largestbidname, ' with $',
                                  orderbook['bids'][i][0], ' * ', askvol - bidvol)
                            print('spread = %.5f' % (orderbook['bids'][i][0] - lowestask))
                            pricediff += (orderbook['bids'][i][0] - lowestask) * (askvol - bidvol)
                            askcost += (askvol - bidvol) * lowestask
                            bidcost += (askvol - bidvol) * orderbook['bids'][i][0]
                            break

                        else:
                            print('buy from ', lowestaskname, ' with $', lowestask, ' sell to ', largestbidname, ' with $',
                                  orderbook['bids'][i][0], ' * ', orderbook['bids'][i][1])
                            print('spread = %.5f' % (orderbook['bids'][i][0] - lowestask))
                            bidvol += orderbook['bids'][i][1]
                            pricediff += (orderbook['bids'][i][0] - lowestask) * orderbook['bids'][i][1]
                            askcost += (orderbook['bids'][i][1]) * lowestask
                            bidcost += (orderbook['bids'][i][1]) * orderbook['bids'][i][0]
                    else:
                        break

        print('pricediff = %.5f' % pricediff)
        askfee = lowestaskname.fees.get('trading')
        bidfee = largestbidname.fees.get('trading')
        print('taker fee = %.5f' % askfee['taker'])
        print('maker fee = %.5f' % bidfee['maker'])
        fee = 0

        if askfee['percentage']:
            fee += askfee['taker'] * askcost
        else:
            fee += askfee['taker']
        if bidfee['percentage']:
            fee += bidfee['taker'] * bidcost
        else:
            fee += bidfee['taker']

        print('total fee = %.5f' % fee)
        print('ask cost = %.5f' % askcost)
        print('bid cost = %.5f\n' % bidcost)

        if (pricediff > fee):
            print(' \n')
            print(' \n')
            print(' \n')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('EXECUTE TRADE: payoff is greater than $ fee \n')

            trades_executed.append(1)
            profit = pricediff - fee
            trades_profit.append(profit)

            print('\n--------- PERFORMANCE ANALYTICS ---------')
            total_profit = np.sum(trades_profit)
            total_trades = np.sum(trades_executed)
            print('Total trades = ', total_trades)
            print('Total profit = ', total_profit)
            print(' \n')

        else:
            pass

    time.sleep(5)


def performance_analytics():
    print('--------- PERFORMANCE ANALYTICS ---------')
    total_profit = np.sum(trades_profit)
    total_trades = np.sum(trades_executed)
    print('Total trades = ', total_trades)
    print('Total profit = ', total_profit)
    print('\n\n')


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
            print("\n---------- Exchange: ", exchange.id, "----------")

        exchange_info = dir(exchange)
        # pprint(exchange_info)
        # print(exchange.symbols)

        # find currency pairs to trade
        pairs = []
        for sym in symbols:
            for symbol in coins:
                if symbol in sym:
                    pairs.append(sym)
        # do not remove:
        # print("Potential Currency Pairs: \n", pairs,"\n")
        # time.sleep(2)


        # from coin 1 to coin 2 - ETH/BTC - Bid
        # from coin 2 to coin 3 - ETH/LTC - Ask
        # from coin 3 to coin 1 - BTC/LTC - Bid
        # arb_list = ['ETH/BTC','ETH/LTC','BTC/LTC']
        arb_list = ['BTC/USD']
        # arb_list = ['BTC/USD','ETH/USD','ETH/BTC']

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
                # print("\n")
                # depth = exchange.fetch_order_book(symbol=sym)
                # pprint(depth)
                time.sleep(0.5)
                # exch_rate_list.append(depth(['bids'][0][0]))
    return (bidlist,asklist)


def run():

    # get_info()

    # initialize()

    # diversify()

    # print("\n\n---------- EXCHANGE FUNDING FEES ----------\n")
    # get_funding_fees()

    # print("\n\n---------- EXCHANGE TRADING FEES ----------\n")
    # get_trading_fees()

    (bidlist, asklist) = arbitrage()
    # portfolio = 10  # BTC
    while 1:
        ActiveTrader(bidlist, asklist)


run()
