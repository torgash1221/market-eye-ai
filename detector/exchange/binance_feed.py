import ccxt


exchange = ccxt.binance({
    "enableRateLimit": True,
    "options": {
        "defaultType": "future"
    }
})


def get_closes(symbol, timeframe, limit):
    candles = exchange.fetch_ohlcv(
        symbol=symbol,
        timeframe=timeframe,
        limit=limit
    )

    closes = [candle[4] for candle in candles]

    return closes
