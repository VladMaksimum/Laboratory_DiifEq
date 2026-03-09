import matplotlib.pyplot as plt
from typing import Sequence
from Function import Function


class Painter:
    def __init__(self, picture_path: str, delta: float):
        self._picture_path = picture_path
        self._delta = delta
    

    def _draw_points(self, x: Sequence, y: Sequence, f: Function) -> None:
        z = f.solve_in_ranges((x, y), self._delta)

        fig, ax = plt.subplots()
        plt.axis('equal')
        plt.grid()

        linetype = '.'

        for i in range(len(y) - 1):
            for j in range(len(x) - 1):
                if abs(z[i][j]) < self._delta:
                    ax.plot(x[j], y[i], linetype)
                if abs(z[i][j + 1]) < self._delta:
                    ax.plot(x[j+1], y[i], linetype)
                if (abs(z[i + 1][j + 1]) < self._delta):
                    ax.plot(x[j+1], y[i+1], linetype)
                if (abs(z[i + 1][j]) < self._delta):
                    ax.plot(x[j], y[i+1], linetype)
        plt.savefig("points.png")



    def draw(self, x: Sequence, y: Sequence, f: Function, line_color: str = 'blue') -> None:
        z = f.solve_in_ranges((x, y), self._delta)

        fig, ax = plt.subplots()
        plt.axis('equal')
        plt.grid()

        for i in range(len(y) - 1):
            for j in range(len(x) - 1):
                pd = (abs(z[i][j]) < self._delta)
                pc = (abs(z[i][j + 1]) < self._delta)
                pb = (abs(z[i + 1][j + 1]) < self._delta)
                pa = (abs(z[i + 1][j]) < self._delta)


                sqrt_code = pa * 8 + pb * 4 + pc * 2 + pd * 1

                ca = (x[j] + self._delta / 2, y[i + 1])
                cb = (x[j+1], y[i] + self._delta / 2)
                cc = (x[j] + self._delta / 2, y[i])
                cd = (x[j], y[i] + self._delta / 2)
                


                match sqrt_code:
                    case 1:
                        ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color)
                    case 2:
                        ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color)
                    case 3:
                        ax.plot([cb[0], cd[0]], [cb[1], cd[1]], line_color)
                    case 4:
                        ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color)
                    case 5:
                        ax.plot([ca[0], cd[0]], [ca[1], cd[1]], line_color)
                        ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color)
                    case 6:
                        ax.plot([cc[0], ca[0]], [cc[1], ca[1]], line_color)
                    case 7:
                        ax.plot([ca[0], cd[0]], [ca[1], cd[1]], line_color)
                    case 8:
                        ax.plot([ca[0], cd[0]], [ca[1], cd[1]], line_color)
                    case 9:
                        ax.plot([cc[0], ca[0]], [cc[1], ca[1]], line_color)
                    case 10:
                        ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color)
                        ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color)
                    case 11:
                        ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color)
                    case 12:
                        ax.plot([cb[0], cd[0]], [cb[1], cd[1]], line_color)
                    case 13:
                        ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color)
                    case 14:
                        ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color)
                
        plt.savefig(self._picture_path)
        