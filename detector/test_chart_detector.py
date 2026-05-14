from detector.chart_renderer import render_chart
from detector.image_detector import detect_image_pattern
from exchange.binance_feed import get_closes


SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "WLDUSDT",
    "DOGEUSDT"
]

TIMEFRAME = "1m"
WINDOW = 100


for symbol in SYMBOLS:
    try:
        closes = get_closes(symbol, TIMEFRAME, WINDOW)

        image_path = render_chart(closes)

        result = detect_image_pattern(image_path)

        similarity = result["similarity"]
        pattern = result["pattern"]

        print(f"{symbol} | {similarity}% | {pattern}")

    except Exception as e:
        print(f"{symbol} | ERROR | {e}")
