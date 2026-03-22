import matplotlib.pyplot as plt
from typing import Sequence
from Function import Function

def interpolate(f1, f2):
    return abs(f1) / (abs(f1) + abs(f2))


class Painter:
    def __init__(self, f: Function, delta: float):
        self._delta = delta
        self._f = f
        self._fig, self._ax = plt.subplots()
        plt.axis('equal')
        plt.grid()

    def _draw_points(self) -> None:
        z = self._f.solve_in_ranges()

        fig, ax = plt.subplots()
        plt.axis('equal')
        plt.grid()

        linetype = '.'

        for i in range(len(self._f._y) - 1):
            for j in range(len(self._f._x) - 1):
                if abs(z[i][j]) < self._delta:
                    ax.plot(self._f._x[j], self._f._y[i], linetype)
                if abs(z[i][j + 1]) < self._delta:
                    ax.plot(self._f._x[j+1], self._f._y[i], linetype)
                if (abs(z[i + 1][j + 1]) < self._delta):
                    ax.plot(self._f._x[j+1], self._f._y[i+1], linetype)
                if (abs(z[i + 1][j]) < self._delta):
                    ax.plot(self._f._x[j], self._f._y[i+1], linetype)
        plt.savefig("points.png")

    def draw_simple(self, parametrs: dict = {}):
        z = self._f.solve_in_ranges(parametrs)

        for i in range(len(self._f._y) - 1):
            for j in range(len(self._f._x) - 1):
                if abs(z[i][j]) < self._delta and abs(z[i][j+1]) < self._delta:
                    self._ax.plot([self._f._x[j], self._f._x[j+1]], [self._f._y[i], self._f._y[i]]) 
                if abs(z[i][j]) < self._delta and abs(z[i+1][j]) < self._delta:
                    self._ax.plot([self._f._x[j], self._f._x[j]], [self._f._y[i], self._f._y[i+1]])
                if abs(z[i][j]) < self._delta and abs(z[i+1][j+1]) < self._delta:
                    self._ax.plot([self._f._x[j], self._f._x[j+1]], [self._f._y[i], self._f._y[i+1]])
    


    def draw(self, line_color: str = 'blue', parametrs: dict = {}) -> None:
        z = self._f.solve_in_ranges(parametrs)

        if 'c' in parametrs.keys():
            c = parametrs['c']
        else:
            c = 0

        for i in range(len(self._f._y) - 1):
            for j in range(len(self._f._x) - 1): 
                pd = z[i][j] >= 0
                pc = z[i][j + 1] >= 0
                pb = z[i + 1][j + 1] >= 0
                pa = z[i + 1][j] >= 0


                sqrt_code = pa * 8 + pb * 4 + pc * 2 + pd * 1

                ca = (self._f._x[j] + self._delta * interpolate(z[i+1][j], z[i+1][j+1]), self._f._y[i + 1])
                cb = (self._f._x[j+1], self._f._y[i] + self._delta  * interpolate(z[i][j+1], z[i+1][j+1]),)
                cc = (self._f._x[j] + self._delta  * interpolate(z[i][j], z[i][j+1]), self._f._y[i])
                cd = (self._f._x[j], self._f._y[i] + self._delta  * interpolate(z[i][j], z[i+1][j]),)
                co = (self._f._x[j] + self._delta / 2, self._f._y[i] + self._delta / 2)


                match sqrt_code:
                    case 1:
                        self._ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color, label=f'c={c}')
                    case 2:
                        self._ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color, label=f'c={c}')
                    case 3:
                        self._ax.plot([cb[0], cd[0]], [cb[1], cd[1]], line_color, label=f'c={c}')
                    case 4:
                        self._ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color, label=f'c={c}')
                    case 5:
                        if self._f.solve_in_point([co[1]], [co[0]], parametrs) <= 0:
                            self._ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color, label=f'c={c}')
                            self._ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color, label=f'c={c}')
                        else:
                            self._ax.plot([ca[0], cd[0]], [ca[1], cd[1]], line_color, label=f'c={c}')
                            self._ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color, label=f'c={c}')
                    case 6:
                        self._ax.plot([cc[0], ca[0]], [cc[1], ca[1]], line_color, label=f'c={c}')
                    case 7:
                        self._ax.plot([ca[0], cd[0]], [ca[1], cd[1]], line_color, label=f'c={c}')
                    case 8:
                        self._ax.plot([ca[0], cd[0]], [ca[1], cd[1]], line_color, label=f'c={c}')
                    case 9:
                        self._ax.plot([cc[0], ca[0]], [cc[1], ca[1]], line_color, label=f'c={c}')
                    case 10:
                        if self._f.solve_in_point([co[1]], [co[0]], parametrs) <= 0:
                            self._ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color, label=f'c={c}')
                            self._ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color, label=f'c={c}')
                        else:
                            self._ax.plot([ca[0], cd[0]], [ca[1], cd[1]], line_color, label=f'c={c}')
                            self._ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color, label=f'c={c}')
                    case 11:
                        self._ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color, label=f'c={c}')
                    case 12:
                        self._ax.plot([cb[0], cd[0]], [cb[1], cd[1]], line_color, label=f'c={c}')
                    case 13:
                        self._ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color, label=f'c={c}')
                    case 14:
                        self._ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color, label=f'c={c}')
                
    def savefig(self, path: str) -> None:
        plt.savefig(path)

    def draw_multiple(self, parametr: list, colors: list[str], p_range: list) -> None:
        for c in range(len(p_range)):
            self.draw(colors[c], {parametr: p_range[c]})