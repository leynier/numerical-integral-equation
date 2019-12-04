from numpy.linalg import cond
from scipy import zeros
from scipy.interpolate import CubicSpline
from scipy.linalg import solve
from gauss import gauss
from roots_legendre_interval import roots_legendre_interval


def integral_equation(K, f, a, b, n = 5, use_python_libs = False):
    x, w = roots_legendre_interval(n, a, b, use_python_libs=use_python_libs)
    matrix = zeros((n, n + 1))
    for i in range(n):
        for j in range(n):
            matrix[i, j] = w[j] * K(x[i], x[j])
        matrix[i, n] = f(x[i])
    y = solve(matrix[:, 0: -1], matrix[:, -1]) if use_python_libs else gauss(matrix)
    assert len(x) == len(y), f'len(x) = {len(x)}, len(y) = {len(y)}'
    result = CubicSpline(x, y)
    return result, cond(matrix)
