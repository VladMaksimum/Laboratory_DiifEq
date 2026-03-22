import matplotlib.pyplot as plt
import numpy as np
from typing import Sequence
from Polar_fucntion import PolarFunction

def to_cartesian(r: float, phi: float):
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    return (x, y)


class PolarPainter:
    def __init__(self, f: PolarFunction, delta: float):
        self._delta = delta
        self._f = f
        self._ax = plt.axes(projection='polar')
        # self._ax.set_yticklabels([])
        self._ax.set_ylim(f._r[0], f._r[-1])
        self._ax.set_aspect('equal')
        #plt.axis('equal')
        #plt.grid()


    def draw_implicit(self, line_color: str = 'blue', parametrs: dict = {}) -> None:
        z = self._f.solve_in_ranges(parametrs)

        for i in range(len(self._f._phi) - 1):
            for j in range(len(self._f._r) - 1):
                pd = z[i][j] >= 0
                pc = z[i][j + 1] >= 0
                pb = z[i + 1][j + 1] >= 0
                pa = z[i + 1][j] >= 0


                sqrt_code = pa * 8 + pb * 4 + pc * 2 + pd * 1

                ca = to_cartesian(self._f._r[j] + self._delta / 2, self._f._phi[i + 1])
                cb = to_cartesian(self._f._r[j+1], self._f._phi[i] + self._delta / 2)
                cc = to_cartesian(self._f._r[j] + self._delta / 2, self._f._phi[i])
                cd = to_cartesian(self._f._r[j], self._f._phi[i] + self._delta / 2)
                co = to_cartesian(self._f._r[j] + self._delta / 2, self._f._phi[i] + self._delta / 2)


                match sqrt_code:
                    case 1:
                        self._ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color)
                    case 2:
                        self._ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color)
                    case 3:
                        self._ax.plot([cb[0], cd[0]], [cb[1], cd[1]], line_color)
                    case 4:
                        self._ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color)
                    case 5:
                        if z[co[1]][co[0]] <= 0:
                            self._ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color)
                            self._ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color)
                        else:
                            self._ax.plot([ca[0], cd[0]], [ca[1], cd[1]], line_color)
                            self._ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color)
                    case 6:
                        self._ax.plot([cc[0], ca[0]], [cc[1], ca[1]], line_color)
                    case 7:
                        self._ax.plot([ca[0], cd[0]], [ca[1], cd[1]], line_color)
                    case 8:
                        self._ax.plot([ca[0], cd[0]], [ca[1], cd[1]], line_color)
                    case 9:
                        self._ax.plot([cc[0], ca[0]], [cc[1], ca[1]], line_color)
                    case 10:
                        if z[co[1]][co[0]] <= 0:
                            self._ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color)
                            self._ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color)
                        else:
                            self._ax.plot([ca[0], cd[0]], [ca[1], cd[1]], line_color)
                            self._ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color)
                    case 11:
                        self._ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color)
                    case 12:
                        self._ax.plot([cb[0], cd[0]], [cb[1], cd[1]], line_color)
                    case 13:
                        self._ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color)
                    case 14:
                        self._ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color)
    
    def _draw_explicit(self, line_color: str = 'blue', parametrs: dict = {}):
        z = self._f.solve_explicit(self._f._phi, parametrs)

        if 'c' in parametrs.keys():
            c = parametrs['c']
        else:
            c = 0

        plt.polar(self._f._phi, z, line_color, label=f'c={c}')
    
    def draw_explicit(self, line_color: str = 'blue', parametrs: dict = {}):
        buffer = 0.001
        phi1 = np.arange(-np.pi / 2 + buffer, np.pi / 2 - buffer, 0.01)
        phi2 = np.arange(np.pi / 2 + buffer, 3*np.pi / 2 - buffer, 0.01)


        for k in range(-6, 6):
            self._f._phi = phi1
            self._draw_explicit(line_color, parametrs={'k':k, **parametrs})
            self._f._phi = phi2
            self._draw_explicit(line_color, parametrs={'k':k, **parametrs})

    def draw_line(self, phi: float, line_color = 'blue'):
        for i in range(len(self._f._r) - 1):
            plt.polar([phi, phi], [self._f._r[i], self._f._r[i+1]], line_color)
            plt.polar([phi + np.pi, phi + np.pi], [self._f._r[i], self._f._r[i+1]], line_color)
                
    def savefig(self, path: str) -> None:
        plt.savefig(path)

    def draw_multiple(self, parametr: str, colors: list[str], p_range: list) -> None:
        for c in range(len(p_range)):
            self.draw_explicit(colors[c], {parametr: p_range[c]})