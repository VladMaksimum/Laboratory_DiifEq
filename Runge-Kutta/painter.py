from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
from functions import funcs
import sys

def func_xy(x, y, fxy):
    return eval(fxy, {}, {'x': x, 'y': y, **funcs})

def func_x(x, fx):
    return eval(fx, {}, {'x': x, **funcs})

def runge_kutta(x: float, y: float, fxy: str, h: float):
    k1 = func_xy(x, y, fxy)
    k2 = func_xy(x + h / 2, y + h/2 * k1, fxy)
    k3 = func_xy(x + h/2, y + h/2 * k2, fxy)
    k4 = func_xy(x + h, y + k3 * h, fxy)

    return y + h * (k1 + 2*k2 + 2*k3 + k4) / 6

def runge_rule(h, x, y, fxy):
    yh = runge_kutta(x, y, fxy, h)
    yh2 = runge_kutta(x, y, fxy, h/2)

    return abs(yh2 - yh) / 15

def draw_graphic(a, b, step, y0, epsilon, fxy, yx):
    fig, ax = plt.subplots()

    x = np.arange(a, b + step, step)
    y_exact = func_x(x, yx)
    plt.plot(x, y_exact, color='red')
    plt.grid()

    y_appr = np.zeros(len(x))
    y_appr[0] = y0
    h = step

    i = 1
    while i < len(x):
        if runge_rule(h, x[i], y_appr[i-1], fxy) >= epsilon:
            i = 1
            h /= 2
            x = np.arange(a, b+step, h)
            y_appr = np.zeros(len(x))
            y_appr[0] = y0
            continue

        y_appr[i] = runge_kutta(x[i], y_appr[i-1], fxy, h)
        i += 1

    for i in range(0, len(x), int(step / h)):
        plt.plot(x[i], y_appr[i], 'go', markersize=4)

    plt.savefig("Runge-Kutta/graphic.png")

    return h, x, y_exact, y_appr