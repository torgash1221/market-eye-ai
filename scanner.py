import time
from datetime import datetime, UTC

from config import SYMBOLS, TIMEFRAME, WINDOW_SIZE, ALERT_THRESHOLD, WATCH_THRESHOLD
from detector.chart_renderer import render_chart
from detector.image_detector import detect_image_pattern
from detector.exchange.binance_feed import get_ohlcv
from telegram_utils import send_telegram_photo, check_telegram_commands


def scan_once():

    for symbol in SYMBOLS:

        try:

            candles = get_ohlcv(symbol, TIMEFRAME, WINDOW_SIZE)

            closes = [candle[4] for candle in candles]

            start_time = datetime.fromtimestamp(
                candles[0][0] / 1000,
                UTC
            ).strftime("%H:%M")

            end_time = datetime.fromtimestamp(
                candles[-1][0] / 1000,
                UTC
            ).strftime("%H:%M")

            image_path = render_chart(candles)

            result = detect_image_pattern(image_path)

            similarity = float(result["similarity"])
            pattern = result["pattern"]

            if similarity >= ALERT_THRESHOLD:

                message = (
                    f"🚨 ALERT\n"
                    f"Symbol: {symbol}\n"
                    f"TF: {TIMEFRAME}\n"
                    f"Range: {start_time} → {end_time} UTC\n"
                    f"Similarity: {similarity}%\n"
                    f"Pattern: {pattern}"
                )

                print(message)

                send_telegram_photo(image_path, message)

            elif similarity >= WATCH_THRESHOLD:

                message = (
                    f"👁 WATCH\n"
                    f"Symbol: {symbol}\n"
                    f"TF: {TIMEFRAME}\n"
                    f"Range: {start_time} → {end_time} UTC\n"
                    f"Similarity: {similarity}%\n"
                    f"Pattern: {pattern}"
                )

                print(message)

                send_telegram_photo(image_path, message)

            else:

                print(f"— {symbol} | {similarity}% | {pattern}")

        except Exception as e:

            print(f"ERROR | {symbol} | {e}")


def run_scanner():

    while True:

        print("\n=== NEW SCAN ===")

        check_telegram_commands()

        scan_once()

        for _ in range(12):

            check_telegram_commands()

            time.sleep(5)


if __name__ == "__main__":

    run_scanner()
