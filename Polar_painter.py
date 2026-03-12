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
        self._fig, self._ax = plt.subplots()
        plt.axis('equal')
        plt.grid()


    def draw(self, line_color: str = 'blue', parametrs: dict = {}) -> None:
        z = self._f.solve_in_ranges(parametrs)

        for i in range(len(self._f._phi) - 1):
            for j in range(len(self._f._r) - 1):
                pd = (abs(z[i][j]) < self._delta)
                pc = (abs(z[i][j + 1]) < self._delta)
                pb = (abs(z[i + 1][j + 1]) < self._delta)
                pa = (abs(z[i + 1][j]) < self._delta)


                sqrt_code = pa * 8 + pb * 4 + pc * 2 + pd * 1

                ca = to_cartesian(self._f._r[j] + self._delta / 2, self._f._phi[i + 1])
                cb = to_cartesian(self._f._r[j+1], self._f._phi[i] + self._delta / 2)
                cc = to_cartesian(self._f._r[j] + self._delta / 2, self._f._phi[i])
                cd = to_cartesian(self._f._r[j], self._f._phi[i] + self._delta / 2)
                


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
                        self._ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color)
                        self._ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color)
                    case 11:
                        self._ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color)
                    case 12:
                        self._ax.plot([cb[0], cd[0]], [cb[1], cd[1]], line_color)
                    case 13:
                        self._ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color)
                    case 14:
                        self._ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color)
                
    def savefig(self, path: str) -> None:
        plt.savefig(path)

    def draw_multiple(self, parametr: str, colors: list[str], p_range: list) -> None:
        for c in range(len(p_range)):
            self.draw(colors[c], {parametr: p_range[c]})