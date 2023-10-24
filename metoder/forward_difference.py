# finner derivert med forward difference

def forward_difference(f, a, h):
    return (f(a + h) - f(a))/h


def f(x):
    return (x-1)**2 + 1


print(forward_difference(f, 2, 0.1))
