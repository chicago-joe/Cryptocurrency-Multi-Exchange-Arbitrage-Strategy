from source.init_exchanges import *
from pprint import pprint
from pprint import pprint

from source.init_exchanges import *


# root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root + '/python')

# logging.basicConfig(level = logging.DEBUG)


def get_info():
    pprint(dir(ccxt.gemini()))
    # pprint(exchange_info)
    # print(exchange.symbols)
