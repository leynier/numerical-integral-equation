from scipy import zeros
from scipy.interpolate import CubicSpline
from gauss import gauss
from roots_legendre_interval import roots_legendre_interval


def integral_equation(K, f, a, b, n = 5):
    x, w = roots_legendre_interval(n, a, b)
    matrix = zeros((n, n + 1))
    for i in range(n):
        for j in range(n):
            matrix[i, j] = w[j] * K(x[i], x[j])
        matrix[i, n] = f(x[i])
    y = gauss(matrix)
    assert len(x) == len(y), f'len(x) = {len(x)}, len(y) = {len(y)}'
    solve = CubicSpline(x, y)
    return solve
