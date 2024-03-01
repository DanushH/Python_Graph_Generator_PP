import numpy as np


def validate_linear(m, c, x_start, x_end):
    try:
        m = float(m)
        c = float(c)
        x_start = float(x_start)
        x_end = float(x_end)
        steps = (x_end - x_start) / 10
        x_values = np.arange(x_start, x_end + steps, steps).round(2).tolist()
        y_values = [round((m * x) + c, 2) for x in x_values]
        return x_values, y_values

    except (TypeError, ValueError):
        return [], []


def validate_quadratic(a, b, c, x_start, x_end):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        x_start = float(x_start)
        x_end = float(x_end)
        steps = (x_end - x_start) / 10
        x_values = np.arange(x_start, x_end + steps, steps).round(2).tolist()
        y_values = [round(a * (x**2) + b * x + c, 2) for x in x_values]
        return x_values, y_values

    except (TypeError, ValueError):
        return [], []
