import time

from config import (
    SYMBOLS,
    TIMEFRAME,
    WINDOW_SIZE,
    ALERT_THRESHOLD,
    WATCH_THRESHOLD
)

from detector.detector import detect_pattern
from exchange.binance_feed import get_closes
from alerts.telegram import send_telegram_message


def scan_once():

    for symbol in SYMBOLS:

        try:
            closes = get_closes(
                symbol,
                TIMEFRAME,
                WINDOW_SIZE
            )

            result = detect_pattern(closes)

            similarity = result["similarity"]
            pattern = result["pattern"]

            # =========================
            # ALERT
            # =========================

            if similarity >= ALERT_THRESHOLD:

                message = (
                    f"🚨 VISUAL PATTERN DETECTED\n\n"
                    f"Symbol: {symbol}\n"
                    f"TF: {TIMEFRAME}\n"
                    f"Similarity: {similarity}%\n"
                    f"Pattern: {pattern}"
                )

                print(message)

                send_telegram_message(message)

            # =========================
            # WATCH
            # =========================

            elif similarity >= WATCH_THRESHOLD:

                print(
                    f"👁 WATCH | "
                    f"{symbol} | "
                    f"{TIMEFRAME} | "
                    f"{similarity}% | "
                    f"{pattern}"
                )

            # =========================
            # NO SIGNAL
            # =========================

            else:

                print(
                    f"— {symbol} | "
                    f"{similarity}% | "
                    f"{pattern}"
                )

        except Exception as e:

            print(f"ERROR | {symbol} | {e}")


def run_scanner():

    while True:

        print("\n=== NEW SCAN ===")

        scan_once()

        time.sleep(60)


if __name__ == "__main__":

    run_scanner()
