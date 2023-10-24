from math import *


def trapezoid_integration(f, a, b, steps):
    area = 0
    step_size = (b - a) / steps
    x = a

    for _ in range(steps):
        area += step_size * (f(x) + f(x + step_size)) / 2
        x += step_size

    return area


def f(x):
    return sqrt(1 + (8*x)**2)


print(trapezoid_integration(f, -(1/2), 2, 100))
