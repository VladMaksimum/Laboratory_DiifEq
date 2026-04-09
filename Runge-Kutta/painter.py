from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
from functions import funcs
import sys

def func_xy(x, y, fxy):
    return eval(fxy, {}, {'x': x, 'y': y, **funcs})

def func_x(x, fx):
    return eval(fx, {}, {'x': x, **funcs})

def runge_kutta(x: float, y: float, fxy: str, h: float) -> float:
    k1 = func_xy(x, y, fxy)
    k2 = func_xy(x + h / 2, y + h/2 * k1, fxy)
    k3 = func_xy(x + h/2, y + h/2 * k2, fxy)
    k4 = func_xy(x + h, y + k3 * h, fxy)

    return y + h * (k1 + 2*k2 + 2*k3 + k4) / 6

def runge_rule(h, x, y, fxy):
    yh = runge_kutta(x, y, fxy, h)
    yh2 = runge_kutta(x + h/2, y, h/2)

    return abs(yh2 - yh) / 15

def euler(h, x, y, fxy):
    return y + func_xy(x, y, fxy) * h

def draw_graphic(a, b, step, y0, epsilon, fxy, yx):
    #print("start", step)
    fig, ax = plt.subplots()

    x = np.arange(a, b + step, step)
    y_exact = func_x(x, yx)
    plt.plot(x, y_exact, color='red', label="аналитическое")
    plt.grid()

    y_appr = np.zeros(len(x))
    yh2 = np.zeros(2*len(x))
    yh2[0] = y0
    y_appr[0] = y0
    h = step

    i = 1
    while i < len(x):
        #print(y_appr[i-1], yh2[2*i-2])

        y_appr[i] = runge_kutta(x[i-1], y_appr[i-1], fxy, h)
        yh2[2*i-1] = runge_kutta(x[i-1], yh2[2*i-2], fxy, h/2)
        yh2[2*i] = runge_kutta(x[i-1] + h/2, yh2[2*i-1], fxy, h/2)

        if abs(y_appr[i] - yh2[2*i]) / 15 >= epsilon:
            i = 1
            h /= 2
            x = np.arange(a, b + h, h)
            y_appr = np.zeros(len(x))
            yh2 = np.zeros(2*len(x))
            yh2[0] = y0
            y_appr[0] = y0

            continue
        

        i += 1
    
    y_appr = yh2
    h /= 2
    x = np.arange(a, b + h, h)

    plt.plot([x[i] for i in range(0, len(x), int(step / h))], [y_appr[i] for i in range(0, len(x), int(step / h))],\
              'go', markersize=4, label="численное")

    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")
    plt.legend()
    plt.savefig("Runge-Kutta/graphic.png")

    #print(h)

    return h, x, y_exact, y_appr

if __name__ == '__main__':
    fxy = 'x + y'
    h = 0.1
    x = np.arange(0, 0.4 + h, h)
    y = np.zeros(len(x))
    y[0] = 1

    for i in range(1, len(x)):
        y[i] = euler(h, x[i-1], y[i-1], fxy)
    
    for j in range(len(x)):
        print(f'{j=} {x[j]=} {y[j]=}')