def simpsons_method(f, a, b, steps):
    area = 0
    h = (b - a) / steps

    if steps % 2 == 0:
        area = simpsons_rule(f, a, b, steps)
    else:
        split_step = (steps - 3) * h

        area += simpsons_rule(f, a, split_step, steps - 3)
        area += simpsons_three_eight_rule(f, split_step, b, 3)

    return area


def simpsons_rule(f, a, b, n):
    area = f(a) + f(b)
    h = (b - a) / n

    for i in range(1, n):
        if i % 2 == 0:
            area += 2 * f(a + (i * h))
        else:
            area += 4 * f(a + (i * h))

    return (h / 3) * area


def simpsons_three_eight_rule(f, a, b, n):
    area = f(a) + f(b)
    h = (b - a) / n

    for i in range(1, n):
        if i % 3 == 0:
            area += 2 * f(a + (i * h))
        else:
            area += 3 * f(a + (i * h))

    return ((3 * h) / 8) * area


def f(x):
    return 6/((6*x**3) - (2*x) + 5)


print(simpsons_method(f, 2, 6, 8))
