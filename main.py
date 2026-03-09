from Function import Function
from Painter import Painter
from Operations import funcs
import numpy as np

expr = input("Input expression:\n")
left, right = expr.split("=")

delta = 0.01
x_s, x_e = -1.5, 1.5
y_s, y_e = -1.5, 1.5

x = np.arange(x_s, x_e, delta)
y = np.arange(y_s, y_e, delta)

f = Function(left, right, ('y', 'z'), funcs)
p = Painter('test.png', delta)

#p._draw_points(x, y, f)

start, end = map(int, input("Input range: ").split())
step = int(input("Input step: "))

for c in range(start, end, step):
    p.draw(x, y, f)