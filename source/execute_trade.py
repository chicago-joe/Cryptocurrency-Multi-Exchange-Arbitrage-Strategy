# root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root + '/python')

# logging.basicConfig(level = logging.DEBUG)


def execute_trade(bidlist, asklist):
    print('EXECUTE TRADE: spread is greater than $ 10 \n')
    trades_executed.append(1)

    for i in range(len(list_of_exchanges)):
        if bidlist[i] > largestbid:
            largestbid = bidlist[i]
        if asklist[i] < lowestask:
            lowestask = asklist[i]
    spread = largestbid - lowestask
    default_trade_fees = 0.05
    profit = spread * (default_trade_fees * spread)
    trades_profit.append(profit)
