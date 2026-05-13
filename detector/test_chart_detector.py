import os
import matplotlib.pyplot as plt


TEMP_DIR = "temp"


def render_chart(closes, output_path="temp/current_chart.png"):
    os.makedirs(TEMP_DIR, exist_ok=True)

    plt.figure(figsize=(6, 4))
    plt.plot(closes, linewidth=2)

    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.savefig(output_path, dpi=100, bbox_inches="tight", pad_inches=0)
    plt.close()

    return output_path
