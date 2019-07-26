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


gemini = ccxt.gemini({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
gemini.apiKey = API_keys.gemini.apiKey
gemini.secret = API_keys.gemini.secret


kraken = ccxt.kraken({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
kraken.apiKey = API_keys.kraken.apiKey
kraken.secret = API_keys.kraken.secret


poloniex = ccxt.poloniex({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
poloniex.apiKey = API_keys.poloniex.apiKey
poloniex.secret = API_keys.poloniex.secret


hitbtc2 = ccxt.hitbtc2({
        'enableRateLimit':True,
})
# enter your API public/secret keys here:
hitbtc2.apiKey = API_keys.hitbtc2.apiKey
hitbtc2.secret = API_keys.hitbtc2.secret

