from source.init_exchanges import *
from pprint import pprint
import time


# import os, sys
# root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root + '/python')

# import logging
# logging.basicConfig(level = logging.DEBUG)


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

