from exchanges.init_exchanges import *
from pprint import pprint
import time
# import os, sys
# root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root + '/python')

# import logging
# logging.basicConfig(level = logging.DEBUG)


def get_trading_fees(list_of_exchanges):
    # exchanges = [bitflyer, bittrex, kraken, gemini]
    for exchange in list_of_exchanges:
        print('EXCHANGE ID: ',exchange.id)
        print('TRADING FEES: ')
        pprint(exchange.fees.get('trading'))
        print('\n')

        # HELP: put in Numpy array to access each exchanges fee as variable?
        # fees = exchanges.fees.get('funding')
        # funding_fees.append(exchanges)

        time.sleep(3)

    return


def get_funding_fees(list_of_exchanges):
    for exchange in list_of_exchanges:
        # print('\n')
        print('EXCHANGE ID: ',exchange.id)
        print('FUNDING FEES: ')
        pprint(exchange.fees.get('funding'))
        print('\n')

        # HELP: put in Numpy array to access each exchanges fee as variable?
        # fees = exchanges.fees.get('funding')
        # funding_fees.append(exchanges)

        time.sleep(3)

    return
