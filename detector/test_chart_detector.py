from detector.chart_renderer import render_chart
from detector.image_detector import detect_image_pattern
from exchange.binance_feed import get_closes


SYMBOL = "BTCUSDT"
TIMEFRAME = "1m"
WINDOW = 100


closes = get_closes(SYMBOL, TIMEFRAME, WINDOW)

image_path = render_chart(closes)

result = detect_image_pattern(image_path)

print(result)
