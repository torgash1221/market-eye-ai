import os
import pandas as pd
import mplfinance as mpf
from datetime import datetime


def render_chart(candles, filename="current_chart.png"):
    os.makedirs("charts", exist_ok=True)

    rows = []

    for candle in candles:
        rows.append({
            "Date": datetime.utcfromtimestamp(candle[0] / 1000),
            "Open": candle[1],
            "High": candle[2],
            "Low": candle[3],
            "Close": candle[4],
            "Volume": candle[5],
        })

    df = pd.DataFrame(rows)
    df.set_index("Date", inplace=True)

    image_path = os.path.join("charts", filename)

    mpf.plot(
        df,
        type="candle",
        style="charles",
        volume=False,
        axisoff=True,
        savefig=dict(fname=image_path, dpi=120, bbox_inches="tight")
    )

    return image_path
