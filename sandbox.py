import matplotlib.pyplot as plt
import numpy as np

def func(x, y):
    return x**3 - y

delta = 0.001
x_s, x_e = -1, 1
y_s, y_e = -1, 1

fig, ax = plt.subplots()
plt.axis('equal')
plt.grid()
ax.set_xlabel("x")
ax.set_ylabel("y")


x = np.arange(x_s, x_e, delta)
y = np.arange(y_s, y_e, delta)
X, Y = np.meshgrid(x, y)

z = func(X, Y) # значения в узлах квадратов

for i in range(len(y) - 1):
    for j in range(len(x) - 1):
        pd = (abs(z[i][j]) < delta)
        pc = (abs(z[i][j + 1]) < delta)
        pb = (abs(z[i + 1][j + 1]) < delta)
        pa = (abs(z[i + 1][j]) < delta)

        sqrt_code = pa * 8 + pb * 4 + pc * 2 + pd * 1

        ca = (x[j] + delta / 2, y[i + 1])
        cb = (x[j+1], y[i] + delta / 2)
        cc = (x[j] + delta / 2, y[i])
        cd = (x[j], y[i] + delta / 2)
        

        match sqrt_code:
            case 1:
                ax.plot([cc[0], cd[0]], [cc[1], cd[1]])
            case 2:
                ax.plot([cc[0], cb[0]], [cc[1], cb[1]])
            case 3:
                ax.plot([cb[0], cd[0]], [cb[1], cd[1]])
            case 4:
                ax.plot([ca[0], cb[0]], [ca[1], cb[1]])
            case 5:
                ax.plot([ca[0], cd[0]], [ca[1], cd[1]])
                ax.plot([cc[0], cb[0]], [cc[1], cb[1]])
            case 6:
                ax.plot([cc[0], ca[0]], [cc[1], ca[1]])
            case 7:
                ax.plot([ca[0], cd[0]], [ca[1], cd[1]])
            case 8:
                ax.plot([ca[0], cd[0]], [ca[1], cd[1]])
            case 9:
                ax.plot([cc[0], ca[0]], [cc[1], ca[1]])
            case 10:
                ax.plot([ca[0], cb[0]], [ca[1], cb[1]])
                ax.plot([cc[0], cd[0]], [cc[1], cd[1]])
            case 11:
                ax.plot([ca[0], cb[0]], [ca[1], cb[1]])
            case 12:
                ax.plot([cb[0], cd[0]], [cb[1], cd[1]])
            case 13:
                ax.plot([cc[0], cb[0]], [cc[1], cb[1]])
            case 14:
                ax.plot([cc[0], cd[0]], [cc[1], cd[1]])
        
plt.savefig("test.png")
