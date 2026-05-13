import time

from config import SYMBOLS, TIMEFRAME, WINDOW_SIZE, ALERT_THRESHOLD, WATCH_THRESHOLD
from detector.detector import detect_pattern
from exchange.binance_feed import get_closes


def scan_once():
    for symbol in SYMBOLS:
        try:
            closes = get_closes(symbol, TIMEFRAME, WINDOW_SIZE)

            result = detect_pattern(closes)

            similarity = result["similarity"]
            pattern = result["pattern"]

            if similarity >= ALERT_THRESHOLD:
                print(f"🚨 ALERT | {symbol} | {TIMEFRAME} | {similarity}% | {pattern}")

            elif similarity >= WATCH_THRESHOLD:
                print(f"👁 WATCH | {symbol} | {TIMEFRAME} | {similarity}% | {pattern}")

            else:
                print(f"— {symbol} | {similarity}% | {pattern}")

        except Exception as e:
            print(f"ERROR | {symbol} | {e}")


def run_scanner():
    while True:
        print("\n=== NEW SCAN ===")
        scan_once()
        time.sleep(60)


if __name__ == "__main__":
    run_scanner()
