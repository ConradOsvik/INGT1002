from math import *


def eulers_method(f, x0: int, y0: int, x_approx: int, n: int):

    h = (x_approx - x0) / n
    x = x0
    y = y0

    for _ in range(n):
        y += h * f(x, y)
        x += h

    return y


def f_der(x, y):
    return y**2 * sin(x)


print(eulers_method(f_der, 0, 1, 1, 2))
