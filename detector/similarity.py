import numpy as np
from detector.normalize import normalize_shape


def correlation_similarity(a, b):
    """
    Сравнение двух форм через correlation.
    Возвращает similarity от 0 до 100.
    """

    a = normalize_shape(a)
    b = normalize_shape(b)

    correlation = np.corrcoef(a, b)[0, 1]

    if np.isnan(correlation):
        return 0

    similarity = (correlation + 1) / 2 * 100

    return round(similarity, 2)
