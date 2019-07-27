from source import API_keys
import ccxt  # noqa: E402


# 'Any Time' CryptoExchange Instantiation
binance = ccxt.binance({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
binance.apiKey = API_keys.binance.apiKey
binance.secret = API_keys.binance.secret


bitflyer = ccxt.bitflyer({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
bitflyer.apiKey = API_keys.bitflyer.apiKey
bitflyer.secret = API_keys.bitflyer.secret

bitfinex = ccxt.bitfinex({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
bitfinex.apiKey = API_keys.bitfinex.apiKey
bitfinex.secret = API_keys.bitfinex.secret


bittrex = ccxt.bittrex({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
bittrex.apiKey = API_keys.bittrex.apiKey
bittrex.secret = API_keys.bittrex.secret


coinbase = ccxt.coinbase({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
coinbase.apiKey = API_keys.coinbase.apiKey
coinbase.secret = API_keys.coinbase.secret

#
# coindeal = ccxt.coindeal({
#         'enableRateLimit':True,
# })
# # enter your API public/secret keys here:
# coindeal.apiKey = API_keys.coindeal.apiKey
# coindeal.secret = API_keys.coindeal.secret


gemini = ccxt.gemini({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
gemini.apiKey = API_keys.gemini.apiKey
gemini.secret = API_keys.gemini.secret

hitbtc = ccxt.hitbtc({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
hitbtc.apiKey = API_keys.hitbtc.apiKey
hitbtc.secret = API_keys.hitbtc.secret


kraken = ccxt.kraken({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
kraken.apiKey = API_keys.kraken.apiKey
kraken.secret = API_keys.kraken.secret

liquid = ccxt.liquid({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
liquid.apiKey = API_keys.liquid.apiKey
liquid.secret = API_keys.liquid.secret


poloniex = ccxt.poloniex({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
poloniex.apiKey = API_keys.poloniex.apiKey
poloniex.secret = API_keys.poloniex.secret
