import ccxt
import time
from exchanges import exchange_fees
from exchanges.init_exchanges import *
# from exchange_fees import get_trading_fees, get_funding_fees
from source import API_keys
import numpy as np
from pprint import pprint

# import os, sys
# root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root + '/python')

# import logging
# logging.basicConfig(level = logging.DEBUG)


list_of_exchanges = [bittrex, bitflyer, liquid, kraken, gemini]
# list_of_exchanges = [bittrex, bitflyer, bitfinex, liquid, poloniex, hitbtc, coinbase, kraken, gemini]

arb_list = ['BTC/USD']
all_symbols = []
trades_executed = []
trades_profit = []


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

    # pull exchanges information here:
            # exchanges = dir(exchanges)
            # pprint(exchanges)
            # print(exchanges.symbols)

            if i > 0:
                break

    except():
        print("\n \n \nATTENTION: NON-VALID CONNECTION WITH CRYPTOCURRENCY BOT\n \n \n")


# active trader - continuous loop of calling trader functions
def ActiveTrader(bid_price_list, ask_price_list):
    is_opportunity = False
    for i in range(len(list_of_exchanges)):
        orderbook = list_of_exchanges[i].fetch_order_book(symbol = arb_list[0])
        if (bid_price_list[i] != orderbook['bids'][0] if len(orderbook['bids']) > 0 else None):
            is_opportunity = True
        if (ask_price_list[i] != orderbook['asks'][0] if len(orderbook['asks']) > 0 else None):
            is_opportunity = True
        bid_price_list[i] = orderbook['bids'][0] if len(orderbook['bids']) > 0 else None
        ask_price_list[i] = orderbook['asks'][0] if len(orderbook['asks']) > 0 else None

    if (is_opportunity == True):
        opportunity(bid_price_list, ask_price_list)

    return (bid_price_list, ask_price_list)


def opportunity(bid_price_list, ask_price_list):
    print('searching for opportunities...')

    highest_bid_price = -1
    lowest_ask_price = 999999999
    highest_bid_id = ''
    lowest_ask_id = ''
    bid_volume = 0
    ask_volume = 0

    for i in range(len(list_of_exchanges)):
        if bid_price_list[i][0] > highest_bid_price:
            highest_bid_id = list_of_exchanges[i]
            highest_bid_price = bid_price_list[i][0]
            bid_volume = bid_price_list[i][1]
        if ask_price_list[i][0] < lowest_ask_price:
            lowest_ask_id = list_of_exchanges[i]
            lowest_ask_price = ask_price_list[i][0]
            ask_volume = ask_price_list[i][1]

    spread = highest_bid_price - lowest_ask_price
    cost_to_buy_at_ask = 0
    cost_to_sell_at_bid = 0

    if (highest_bid_price > lowest_ask_price):
        if bid_volume > ask_volume:
            print('Opportunity: Buy from ', lowest_ask_id, ' with $', lowest_ask_price, ' Sell to ', highest_bid_id, ' with $',
                  highest_bid_price, ' * ',
                  ask_volume)
            print('Bid/Ask Spread = %.5f' % spread)
            cost_to_buy_at_ask += ask_volume * lowest_ask_price
            cost_to_sell_at_bid += ask_volume * highest_bid_price
            price_difference = spread * ask_volume
            orderbook = lowest_ask_id.fetch_order_book(symbol = 'BTC/USD')
            for i in range(len(orderbook['asks'])):
                if (i != 0):
                    if highest_bid_price > orderbook['asks'][i][0]:
                        if (ask_volume + orderbook['asks'][i][1] >= bid_volume):
                            print('Buy from ', lowest_ask_id, ' with $', orderbook['asks'][i][0], ' Sell to ', highest_bid_id, ' with $',
                                  highest_bid_price, ' * ', bid_volume - ask_volume)
                            print('Bid/Ask Spread = %.5f' % (highest_bid_price - orderbook['asks'][i][0]))
                            price_difference += (highest_bid_price - orderbook['asks'][i][0]) * (bid_volume - ask_volume)
                            cost_to_buy_at_ask += (bid_volume - ask_volume) * orderbook['asks'][i][0]
                            cost_to_sell_at_bid += (bid_volume - ask_volume) * highest_bid_price
                            break
                        else:
                            print('Buy from ', lowest_ask_id, ' with $', orderbook['asks'][i][0], ' Sell to ', highest_bid_id, ' with $',
                                  highest_bid_price, ' * ', orderbook['asks'][i][1])
                            print('Bid/Ask Spread = %.5f' % (highest_bid_price - orderbook['asks'][i][0]))
                            ask_volume += orderbook['asks'][i][1]
                            price_difference += (highest_bid_price - orderbook['asks'][i][0]) * orderbook['asks'][i][1]
                            cost_to_buy_at_ask += orderbook['asks'][i][1] * orderbook['asks'][i][0]
                            cost_to_sell_at_bid += orderbook['asks'][i][1] * highest_bid_price
                    else:
                        break
        else:
            print('Opportunity: Buy from ', lowest_ask_id, ' with $', lowest_ask_price, ' Sell to ', highest_bid_id, ' with $',
                  highest_bid_price, ' * ',
                  bid_volume)
            print('Bid/Ask Spread = %.5f' % spread)
            cost_to_buy_at_ask += bid_volume * lowest_ask_price
            cost_to_sell_at_bid += bid_volume * highest_bid_price
            price_difference = spread * bid_volume
            orderbook = highest_bid_id.fetch_order_book(symbol = 'BTC/USD')

            for i in range(len(orderbook['bids'])):
                if (i != 0):
                    if orderbook['bids'][i][0] > lowest_ask_price:
                        if (bid_volume + orderbook['bids'][i][1] >= ask_volume):
                            print('Buy from ', lowest_ask_id, ' with $', lowest_ask_price, ' Sell to ', highest_bid_id, ' with $',
                                  orderbook['bids'][i][0], ' * ', ask_volume - bid_volume)
                            print('Bid/Ask Spread = %.5f' % (orderbook['bids'][i][0] - lowest_ask_price))
                            price_difference += (orderbook['bids'][i][0] - lowest_ask_price) * (ask_volume - bid_volume)
                            cost_to_buy_at_ask += (ask_volume - bid_volume) * lowest_ask_price
                            cost_to_sell_at_bid += (ask_volume - bid_volume) * orderbook['bids'][i][0]
                            break

                        else:
                            print('Buy from ', lowest_ask_id, ' with $', lowest_ask_price, ' Sell to ', highest_bid_id, ' with $',
                                  orderbook['bids'][i][0], ' * ', orderbook['bids'][i][1])
                            print('Bid/Ask Spread = %.5f' % (orderbook['bids'][i][0] - lowest_ask_price))

                            bid_volume += orderbook['bids'][i][1]
                            price_difference += (orderbook['bids'][i][0] - lowest_ask_price) * orderbook['bids'][i][1]

                            cost_to_buy_at_ask += (orderbook['bids'][i][1]) * lowest_ask_price
                            cost_to_sell_at_bid += (orderbook['bids'][i][1]) * orderbook['bids'][i][0]
                    else:
                        break

        print('Price Difference = %.5f' % price_difference, '\n')

        liquid_exch_trading_fees = dict({ 'trading':{ 'percentage':True, 'taker':0.001, 'maker':0.001 },
                                          'funding':{ 'withdraw':{ }, 'deposit':{ } } })
        liquid.fees = liquid_exch_trading_fees

        if lowest_ask_id == liquid:
            ask_fee = liquid.fees.get('trading')
            bid_fee = highest_bid_id.fees.get('trading')
            print('--- Trade Fees ---')
            print('Taker Fee = %.5f' % ask_fee['taker'])
            print('Maker Fee = %.5f' % bid_fee['maker'])
        elif highest_bid_id == liquid:
            ask_fee = lowest_ask_id.fees.get('trading')
            bid_fee = liquid.fees.get('trading')
            print('--- Trade Fees ---')
            print('Taker Fee = %.5f' % ask_fee['taker'])
            print('Maker Fee = %.5f' % bid_fee['maker'])
        else:
            ask_fee = lowest_ask_id.fees.get('trading')
            bid_fee = highest_bid_id.fees.get('trading')
            print('--- Trade Fees ---')
            print('Taker Fee = %.5f' % ask_fee['taker'])
            print('Maker Fee = %.5f' % bid_fee['maker'])

        trade_fees = 0
        if ask_fee['percentage']:
            trade_fees += ask_fee['taker'] * cost_to_buy_at_ask
        else:
            trade_fees += ask_fee['taker']
        if bid_fee['percentage']:
            trade_fees += bid_fee['taker'] * cost_to_sell_at_bid
        else:
            trade_fees += bid_fee['taker']
        print('Cost to buy at Ask = %.5f' % cost_to_buy_at_ask)
        print('Cost to sell at Bid = %.5f' % cost_to_sell_at_bid,'\n')
        print('Total Transaction Cost = %.5f' % trade_fees,'\n\n')

        if (price_difference > trade_fees):
            print(' \n')
            print(' \n')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('EXECUTE TRADE: PAYOFF IS GREATER THAN TRANSACTION COST ')

            trades_executed.append(1)
            profit = price_difference - trade_fees
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

    bid_price_list = []
    ask_price_list = []

    for exchange in list_of_exchanges:
        symbols = exchange.load_markets()
        if symbols is None:
            print("\n----------------\nNext Exchange\n----------------")
        elif len(symbols) < 5:
            print("\n----------------\nMore Symbol Pairs Required\n----------------")
        else:
            print("\n---------- Exchange: ", exchange.id, "----------")

        for sym in arb_list:
            if sym in symbols:
                orderbook = exchange.fetch_order_book(symbol = sym)

                bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
                ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
                bid_price_list.append(bid)
                ask_price_list.append(ask)

                spread = (ask - bid) if (bid and ask) else None

                data = ('Top of Book Prices ', { 'Bid Price':bid, 'Ask Price':ask, 'Bid/Ask Spread':spread })
                pprint(data)
                time.sleep(0.5)

    return (bid_price_list, ask_price_list)


def run():
    # get_info()
    # initialize()
    # diversify()

    # print("\n\n---------- EXCHANGE FUNDING FEES ----------\n")
    # get_funding_fees(list_of_exchanges)

    # print("\n\n---------- EXCHANGE TRADING FEES ----------\n")
    # get_trading_fees(list_of_exchanges)

    (bid_price_list, ask_price_list) = arbitrage()
    # portfolio = 10  # BTC

    while 1:
        ActiveTrader(bid_price_list, ask_price_list)


run()
