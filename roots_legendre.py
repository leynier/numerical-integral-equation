from scipy import array
from scipy.special import legendre


def roots_legendre(n):
    """
    Computes the sample points and weights for Gauss-Legendre quadrature.
    The sample points are the roots of the n-th degree Legendre polynomial
    `P_n(x)`.  These sample points and weights correctly integrate
    polynomials of degree `2n - 1` or less over the interval
    `[-1, 1]` with weight function `f(x) = 1.0`.

    Parameters
    ----------
    n : int
        quadrature order

    Returns
    -------
    x : ndarray
        Sample points
    w : ndarray
        Weights
    """
    p = legendre(n + 1)
    x = legendre(n).roots
    w = 2 * (1 - x ** 2) / ((n + 1) ** 2 * p(x) ** 2)
    temp = list(zip(x, w))
    temp.sort()
    x, w = array([i for i, _ in temp]), array([i for _, i in temp])
    return x, w
