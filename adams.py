from euler import euler_method


def adams_method(f, a, b, y0, h):
    """ Метод Адамса """
    n = int((b - a) / h)
    b0 = min(b, a + 3 * h)
    dots = euler_method(f, a, b0, y0, h)

    for i in range(4, n + 1):
        df = f(dots[i - 1][0], dots[i - 1][1]) - f(dots[i - 2][0], dots[i - 2][1])
        d2f = f(dots[i - 1][0], dots[i - 1][1]) - 2 * f(dots[i - 2][0], dots[i - 2][1]) + \
              f(dots[i - 3][0], dots[i - 3][1])
        d3f = f(dots[i - 1][0], dots[i - 1][1]) - 3 * f(dots[i - 2][0], dots[i - 2][1]) + \
              3 * f(dots[i - 3][0], dots[i - 3][1]) - f(dots[i - 4][0], dots[i - 4][1])
        dots.append((dots[i - 1][0] + h,
                     dots[i - 1][1] + h * f(dots[i - 1][0], dots[i - 1][1]) +
                     (h ** 2) * df / 2 + 5 * (h ** 3) * d2f / 12 + 3 * (h ** 4) * d3f / 8))

    return dots
