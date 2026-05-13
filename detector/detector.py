import json
import os

from detector.similarity import correlation_similarity
from config import PATTERN_FOLDER


def load_patterns():
    patterns = []

    for file_name in os.listdir(PATTERN_FOLDER):

        if not file_name.endswith(".json"):
            continue

        path = os.path.join(PATTERN_FOLDER, file_name)

        with open(path, "r") as f:
            data = json.load(f)

            patterns.append({
                "name": data["name"],
                "values": data["values"]
            })

    return patterns


def detect_pattern(current_values):

    patterns = load_patterns()

    best_match = None
    best_score = 0

    for pattern in patterns:

        score = correlation_similarity(
            current_values,
            pattern["values"]
        )

        if score > best_score:
            best_score = score
            best_match = pattern["name"]

    return {
        "pattern": best_match,
        "similarity": round(best_score, 2)
    }
