from source import API_keys
from source.init_exchanges import *
from pprint import pprint
import ccxt
import time


def get_trading_fees():
    exchanges = [bitflyer, bittrex, kraken, gemini]
    for exchange in exchanges:
        print('EXCHANGE ID: ',exchange.id)
        print('TRADING FEES: ')
        pprint(exchange.fees.get('trading'))
        print('\n')

        # HELP: put in Numpy array to access each exchange fee as variable?
        # fees = exchange.fees.get('funding')
        # funding_fees.append(exchange)

        time.sleep(3)

    return


def get_funding_fees():
    exchanges = [bitflyer, bittrex, kraken, gemini]
    for exchange in exchanges:
        # print('\n')
        print('EXCHANGE ID: ',exchange.id)
        print('FUNDING FEES: ')
        pprint(exchange.fees.get('funding'))
        print('\n')

        # HELP: put in Numpy array to access each exchange fee as variable?
        # fees = exchange.fees.get('funding')
        # funding_fees.append(exchange)

        time.sleep(3)

    return

