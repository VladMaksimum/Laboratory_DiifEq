from typing import Callable
import numpy as np
import matplotlib.pyplot as plt

def runge_kutta(x: float, y: float, f: Callable, h: float):
    k1 = f(x, y)
    k2 = f(x + h / 2, y + h/2 * k1)
    k3 = f(x + h/2, y + h/2 * k2)
    k4 = f(x + h, y + k3 * h)

    return y + h * (k1 + 2*k2 + 2*k3 + k4) / 6

def func1(x, y):
    return -y**2 - x**(-4)

def func2(x):
    return (np.tan(1/x - 1) + x) / (x**2)

def runge_rule(h, x, y, f):
    yh = runge_kutta(x, y, f, h)
    yh2 = runge_kutta(x, y, f, h/2)

    return abs(yh2 - yh) / 15


a = 1
b = 2
step = 0.1

x = np.arange(a, b + step, step)
y_exact = func2(x)
plt.plot(x, y_exact, color='red')
plt.grid()

y0 = 1
y_appr = np.zeros(len(x))
y_appr[0] = y0
fxy = func1
h = step

i = 1
epsilon = 10**(-6)
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
    print(f'x[i]={float(x[i]):.1f} y[i]={y_appr[i]} y={y_exact[int(i*h / step)]} diff={abs(y_appr[i] - y_exact[int(i*h / step)])}')

print(h)
plt.show()