from Function import Function
from Painter import Painter
from Operations import funcs
import numpy as np

expr = input("Input expression:\n")
left, right = expr.split("=")

delta = 0.01
x_s, x_e = -1, 1
y_s, y_e = -1, 1

x = np.arange(x_s, x_e, delta)
y = np.arange(y_s, y_e, delta)

f = Function(left, right, ('x', 'y'), funcs)
p = Painter('test.png', delta)

z = f.solve_in_ranges((x, y), delta)

p.draw(x, y, z)