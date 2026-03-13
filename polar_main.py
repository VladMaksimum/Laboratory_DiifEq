from Polar_fucntion import PolarFunction
from Polar_painter import PolarPainter
from Operations import funcs
import numpy as np

expr = input("Input expression:\n")
left, right = expr.split("=")

base_pict_path = 'pictures/'
step = 0.01
r_s, r_e = -2, 2
phi_s, phi_e = 0, 2*np.pi
buffer = 0.001

r = np.arange(r_s, r_e, step)
phi1 = np.arange(-np.pi / 2 + buffer, np.pi / 2 - buffer, step)
phi2 = np.arange(np.pi / 2 + buffer, 3*np.pi / 2 - buffer, step)
phis = [phi1, phi2]

f = PolarFunction(left, right, ('r', 'phi'), funcs, r, phis[0])
p = PolarPainter(f, step)

#p._draw_points(x, y, f)

#start, end = map(int, input("Input range: ").split())
#step = int(input("Input step: "))

'''
p.draw()
p._f._phi = phi2
p.draw()
p.savefig(f'{base_pict_path}polar_test.png')
'''


#p.draw_multiple("c", ['blue', 'red', 'green'], [1, 2,  3])

#p.savefig(f'{base_pict_path}multi_pict.png')


p.draw_multiple("k", ['blue' for _ in range(-6, 6)], range(-6, 6))
p._f._phi = phi2
p.draw_multiple("k", ['blue' for _ in range(-6, 6)], range(-6, 6))

p.savefig(f'{base_pict_path}multi_polar.png')