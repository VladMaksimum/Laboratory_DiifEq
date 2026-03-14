from Function import Function
from Polar_fucntion import PolarFunction
from Polar_painter import PolarPainter
from Painter import Painter
from Operations import funcs
import numpy as np


class Interface:
    def draw_cartesian(self, save_file: str):
        expr = input("Input expression:\n")
        left, right = expr.split("=")
        consts = input("Input constants: ")

        try:
            consts = list(map(int, consts.split()))
        except:
            consts = [int(consts)]

        base_pict_path = 'pictures/'
        step = 0.01
        buffer = 0.001

        x_s, x_e = map(int, input("Input x range: ").split())
        y_s, y_e = map(int, input("Input y range: ").split())

        x1 = np.arange((x_e + x_s) / 2 + buffer, x_e, step)
        x2 = np.arange(x_s, (x_e + x_s) / 2 - buffer, step)
        y = np.arange(y_s, y_e, step)

        f = Function(left, right, ('x', 'y'), funcs, x1, y)
        p = Painter(f, step)

        colors = ['blue', 'red', 'green']

        for k in range(-6, 6):
            for i, c in enumerate(consts):
                p.draw(line_color=colors[i%3], parametrs={'k': k, 'c': c})

        p._f._x = x2
        for k in range(-6, 6):
            for i, c in enumerate(consts):
                p.draw(line_color=colors[i%3], parametrs={'k': k, 'c': c})

        p.savefig(f'{base_pict_path}{save_file}')
    
    def draw_polar(self, save_file: str):
        expr = input("Input expression:\n")
        left, right = expr.split("=")
        consts = input("Input constants: ")

        try:
            consts = list(map(int, consts.split()))
        except:
            consts = [int(consts)]

        base_pict_path = 'pictures/'
        step = 0.01
        buffer = 0.001

        r_s, r_e = map(int, input("Input r range: ").split())

        phi1 = np.arange(-np.pi / 2 + buffer, np.pi / 2 - buffer, step)
        phi2 = np.arange(np.pi / 2 + buffer, 3*np.pi / 2 - buffer, step)
        r = np.arange(r_s, r_e, step)

        f = PolarFunction(left, right, ('r', 'phi'), funcs, r, phi1)
        p = PolarPainter(f, step)

        colors = ['blue', 'red', 'green']

        for k in range(-6, 6):
            for i, c in enumerate(consts):
                p.draw(line_color=colors[i%3], parametrs={'k': k, 'c': c})

        p._f._phi = phi2
        for k in range(-6, 6):
            for i, c in enumerate(consts):
                p.draw(line_color=colors[i%3], parametrs={'k': k, 'c': c})

        p.savefig(f'{base_pict_path}{save_file}')
    