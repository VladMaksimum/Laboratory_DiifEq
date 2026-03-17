import numpy as np
import matplotlib.pyplot as plt
from Polar_fucntion import PolarFunction
from Polar_painter import PolarPainter
from Operations import funcs

r = np.arange(-1, 1, 0.01)
buffer = 0.001
phi1 = np.arange(-np.pi / 2 + buffer, np.pi / 2 - buffer, 0.01)
phi2 = np.arange(np.pi / 2 + buffer, 3*np.pi / 2 - buffer, 0.01)

f = PolarFunction('r', 'sqrt(exp(arctg(2*tg(phi)) + pi*k) / (1 + 3*(sin(phi))**2))', ('r', 'phi'), funcs, r, phi1)
p = PolarPainter(f, 0.01)


p.draw_explicit()
plt.savefig("explicit.png")

