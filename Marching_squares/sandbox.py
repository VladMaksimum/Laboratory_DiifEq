import numpy as np
import matplotlib.pyplot as plt
from Function import Function
from Polar_fucntion import PolarFunction
from Polar_painter import PolarPainter
from Painter import Painter
from Operations import funcs

expr = input("Input expression:\n")
left, right = expr.split("=")
consts = input("Input constants: ")

try:
    consts = list(map(float, consts.split()))
except:
    consts = [float(consts)]

base_pict_path = 'pictures/'
step = 0.001
buffer = 0.001

x_s, x_e = map(float, input("Input x range: ").split())
y_s, y_e = map(float, input("Input y range: ").split())

#x1 = np.arange((x_e + x_s) / 2 + buffer, x_e, step)
#x2 = np.arange(x_s, (x_e + x_s) / 2 - buffer, step)
y = np.arange(y_s, y_e, step)
x = np.arange(x_s, x_e, step)

f = Function(left, right, ('x', 'y'), funcs, x, y)
p = Painter(f, step)

colors = ['blue', 'red', 'green']


for i, c in enumerate(consts):
    p.draw(colors[i%3], {'c': c})
    p.draw(colors[i%3], {'c': (-c)})

p._f._expr = 'x + y - 2'
p.draw()


'''
p._f._x = x2
for k in range(-6, 6):
    for i, c in enumerate(consts):
        p.draw(line_color=colors[i%3], parametrs={'k': k, 'c': c})
        '''


p.savefig(f'{base_pict_path}{'test2.png'}')

