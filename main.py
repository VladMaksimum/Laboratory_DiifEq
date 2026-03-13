from Function import Function
from Painter import Painter
from Operations import funcs
import numpy as np

expr = input("Input expression:\n")
left, right = expr.split("=")

base_pict_path = 'pictures/'
step = 0.01
buffer = 0.001
x_s, x_e = -2, 2
y_s, y_e = -2, 2

x1 = np.arange(buffer, x_e, step)
x2 = np.arange(x_s, -buffer, step)
y1 = np.arange(buffer, y_e, step)
y2 = np.arange(y_s, -buffer, step)

ys = [y1, y2]
xs = [x1, x2]
'''
f = Function(left, right, ('y', 'z'), funcs, x, y)
p = Painter(f, step)

#p._draw_points(x, y, f)

#start, end = map(int, input("Input range: ").split())
#step = int(input("Input step: "))

#p.draw()
#p.savefig(f'{base_pict_path}test.png')


p.draw_multiple("k", ['blue' for _ in range(-6, 6)], range(-6, 6))

p.savefig(f'{base_pict_path}multi_pict.png')
'''
p = Painter(None, step)

for p1 in range(2):
    for p2 in range(2):
        f = Function(left, right, ('y', 'z'), funcs, xs[p1], ys[p2])
        p._f = f

        p.draw_multiple("k", ['blue' for _ in range(-6, 6)], range(-6, 6))

p.savefig(f'{base_pict_path}multi_pict.png')