# -*- coding: utf-8 -*-

import os
import sys
from pprint import pprint


root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt  # noqa: E402

# return up to ten bidasks on each side of the order book stack
limit = 10
pprint(ccxt.cex().fetch_order_book('BTC/USD', limit))
