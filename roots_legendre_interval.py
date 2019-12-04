from roots_legendre import roots_legendre


def roots_legendre_interval(n, a, b):
    """
    Computes the sample points and weights for Gauss-Legendre quadrature
    on interval `[a, b]`.
    The sample points are the roots of the n-th degree Legendre polynomial
    `P_n(x)`.  These sample points and weights correctly integrate
    polynomials of degree `2n - 1` or less over the interval
    `[-1, 1]` with weight function `f(x) = 1.0`.

    Parameters
    ----------
    n : int
        quadrature order
    a : int
        limit inf
    b: int
        limit sup
    Returns
    -------
    x : ndarray
        Sample points
    w : ndarray
        Weights
    """
    x, w = roots_legendre(n)
    x = 0.5 * (b - a) * x + 0.5 * (b + a)
    w = 0.5 * (b - a) * w
    return x, w
