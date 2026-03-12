from Polar_fucntion import PolarFunction
from Polar_painter import PolarPainter
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

f = PolarFunction(left, right, ('r', 'phi'), funcs, x, y)
p = PolarPainter(f, delta)

#p._draw_points(x, y, f)

#start, end = map(int, input("Input range: ").split())
#step = int(input("Input step: "))

p.draw()
p.savefig(f'{base_pict_path}polar_test.png')


#p.draw_multiple("c", ['blue', 'red', 'green'], [1, 2,  3])

#p.savefig(f'{base_pict_path}multi_pict.png')