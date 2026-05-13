import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


PATTERNS_DIR = "patterns"


def load_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Не удалось открыть изображение: {path}")

    img = cv2.resize(img, (300, 200))
    img = cv2.GaussianBlur(img, (3, 3), 0)
    return img


def compare_images(img1, img2):
    score = ssim(img1, img2)
    return round(score * 100, 2)


def detect_image_pattern(current_image_path):
    current_img = load_image(current_image_path)

    best_score = 0
    best_pattern = None

    for filename in os.listdir(PATTERNS_DIR):
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        pattern_path = os.path.join(PATTERNS_DIR, filename)
        pattern_img = load_image(pattern_path)

        score = compare_images(current_img, pattern_img)

        if score > best_score:
            best_score = score
            best_pattern = filename

    return {
        "similarity": best_score,
        "pattern": best_pattern
    }
