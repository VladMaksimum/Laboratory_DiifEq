import numpy as np
import matplotlib.pyplot as plt

def func(x, y):
    if abs(x) < 10**(-6) or abs(y) < 10**(-6):
        return float('nan')
    
    return (np.log1p((x**2 + 4*y**2) - 1) - np.atan(2*y / x))

def interpolate(x1, x2, v1, v2):
    return (x1 + ((-v2) / v1) * abs(x2-x1))

def draw(z, x, y, step, fig, ax):

    for i in range(len(y) - 1):
        for j in range(len(x) - 1): 
            pd = z[i][j] > 0
            pc = z[i][j + 1] > 0
            pb = z[i + 1][j + 1] > 0
            pa = z[i + 1][j] > 0


            sqrt_code = pa * 8 + pb * 4 + pc * 2 + pd * 1

            ca = (x[j] + step / 2, y[i + 1])
            cb = (x[j+1], y[i] + step / 2)
            cc = (x[j] + step / 2, y[i])
            cd = (x[j], y[i] + step / 2)
            co = (x[j] + step / 2, y[i] + step / 2)
            co = (x[j] + step / 2, y[i] + step / 2)
            
            line_color = 'blue'

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
                    if z[co[1]][co[0]] <= 0:
                        ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color)
                        ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color)
                    else:
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
                    if z[co[1]][co[0]] <= 0:
                        ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color)
                        ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color)
                    else:
                        ax.plot([ca[0], cd[0]], [ca[1], cd[1]], line_color)
                        ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color)
                case 11:
                    ax.plot([ca[0], cb[0]], [ca[1], cb[1]], line_color)
                case 12:
                    ax.plot([cb[0], cd[0]], [cb[1], cd[1]], line_color)
                case 13:
                    ax.plot([cc[0], cb[0]], [cc[1], cb[1]], line_color)
                case 14:
                    ax.plot([cc[0], cd[0]], [cc[1], cd[1]], line_color)

x_s, x_e = -2, 2
y_s, y_e = -2, 2
step = 0.01

x1 = np.arange(step, x_e, step)
x2 = np.arange(x_s, -step, step)
y1 = np.arange(step, y_e, step)
y2 = np.arange(y_s, -step, step)

ys = [y1, y2]
xs = [x1, x2]

fig, ax = plt.subplots()

for p1 in range(2):
    for p2 in range(2):
        z = [[0 for _ in range(len(xs[p1]))] for _ in range(len(ys[p2]))]

        for i in range(len(xs[p1])):
            for j in range(len(ys[p2])):
                z[j][i] = func(xs[p1][i], ys[p2][j])

        draw(z, xs[p1], ys[p2], step, fig, ax)

plt.savefig("full_new_test.png")

