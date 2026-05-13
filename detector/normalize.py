import numpy as np


def normalize_shape(values, target_length=50):
    """
    Нормализует форму графика:
    - приводит к одинаковой длине
    - масштабирует значения от 0 до 1
    """

    values = np.array(values, dtype=float)

    # Интерполяция длины
    x_old = np.linspace(0, 1, len(values))
    x_new = np.linspace(0, 1, target_length)

    resized = np.interp(x_new, x_old, values)

    # Нормализация
    min_val = resized.min()
    max_val = resized.max()

    if max_val - min_val == 0:
        return np.zeros(target_length)

    normalized = (resized - min_val) / (max_val - min_val)

    return normalized
