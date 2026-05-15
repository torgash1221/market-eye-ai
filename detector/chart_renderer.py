import os
import pandas as pd
import mplfinance as mpf
from datetime import datetime, UTC


def render_chart(candles, filename="current_chart.png"):

    os.makedirs("charts", exist_ok=True)

    rows = []

    for candle in candles:

        rows.append({
            "Date": datetime.fromtimestamp(candle[0] / 1000, UTC),
            "Open": float(candle[1]),
            "High": float(candle[2]),
            "Low": float(candle[3]),
            "Close": float(candle[4]),
            "Volume": float(candle[5]),
        })

    df = pd.DataFrame(rows)

    df.set_index("Date", inplace=True)

    image_path = os.path.join("charts", filename)

    mpf.plot(
        df,
        type="candle",
        style="charles",
        volume=False,
        figsize=(8, 5),
        tight_layout=True,
        axisoff=True,
        savefig=dict(
            fname=image_path,
            dpi=150,
            bbox_inches="tight",
            pad_inches=0
        )
    )

    return image_path
