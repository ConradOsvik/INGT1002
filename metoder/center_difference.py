def center_difference(f, a, h):
    return (f(a + h) - f(a - h)) / 2*h


def f(x):
    return (x-2)**2 + 1


print(center_difference(f, 2, 0.1))
