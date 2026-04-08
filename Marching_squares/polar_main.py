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
step = 0.01
buffer = 0.001

x_s, x_e = map(float, input("Input r range: ").split())
y_s, y_e = map(float, input("Input phi range: ").split())

#x1 = np.arange((x_e + x_s) / 2 + buffer, x_e, step)
#x2 = np.arange(x_s, (x_e + x_s) / 2 - buffer, step)
phi1 = np.arange(y_s, y_e, step)
phi2 = np.arange(4.61, 6.28, step)
r = np.arange(x_s, x_e, step)

f = PolarFunction(left, right, ('r', 'phi'), funcs, r, phi1)
p = PolarPainter(f, step)

colors = ['blue', 'red', 'green']


for i, c in enumerate(consts):
    p.draw_implicit(line_color=colors[i%3], parametrs={'c': c})
    p.draw_implicit(line_color=colors[i%3], parametrs={'c': -c})



'''p.draw_line(-np.pi / 4, line_color='purple')
p.draw_line(np.atan(4), line_color='purple')'''


'''
p._f._x = x2
for k in range(-6, 6):
    for i, c in enumerate(consts):
        p.draw(line_color=colors[i%3], parametrs={'k': k, 'c': c})
        '''


p.savefig(f'{base_pict_path}{'test2.png'}')

