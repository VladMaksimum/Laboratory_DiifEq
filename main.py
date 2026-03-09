from Function import Function
from Painter import Painter
from Operations import funcs
import numpy as np

expr = input("Input expression:\n")
left, right = expr.split("=")

base_pict_path = 'pictures/'
delta = 0.01
x_s, x_e = -5, 5
y_s, y_e = -5, 5

x = np.arange(x_s, x_e, delta)
y = np.arange(y_s, y_e, delta)

f = Function(left, right, ('y', 'z'), funcs, x, y)
p = Painter(f, delta)

#p._draw_points(x, y, f)

#start, end = map(int, input("Input range: ").split())
#step = int(input("Input step: "))

#p.draw(f'{base_pict_path}test.png')

p.draw_multiple("c", ['blue', 'red', 'green'], [1, 2,  3])

p.savefig(f'{base_pict_path}multi_pict.png')