import pandas as pd
import talib.

from logbook import Logger, INFO

from catalyst import run_algorithm
from catalyst.api import order, symbol, record
from catalyst.exchange.utils.stats_utils import get_pretty_stats, \
    extract_transactions

log = Logger('simple_loop', level=INFO)


from catalyst.api import order, record, symbol

def initialize(context):
    context.asset = symbol('btc_usd')

def handle_data(context, data):
    order(context.asset, 1)
    record(btc = data.current(context.asset, 'price'))

catalyst ingest-exchange -x bitfinex -i btc_usd
