# Constructor and selectors
#
# def rational(n, d):
#     """A representation of the rational number N/D."""
#     return [n, d]
#
#
# def numer(x):
#     """Return the numerator of rational number X."""
#     return x[0]
#
#
# def denom(x):
#     """Return the denominator of rational number X."""
#     return x[1]


# Rational arithmetic

def add_rational(x, y):
    """The sum of rational numbers X and Y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def mul_rational(x, y):
    """The product of rational numbers X and Y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))


def rationals_are_equal(x, y):
    """True iff rational numbers X and Y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)


def print_rational(x):
    """Print rational X."""
    print(numer(x), "/", denom(x))


# Improved specification

from math import gcd


def rational(n: int, d: int) -> list:
    """A representation of the rational number N/D."""
    g = gcd(n, d)
    return [n // g, d // g]


def numer(x):
    """Return the numerator of rational number X in lowest terms and having
    the sign of X."""
    return x[0]


def denom(x):
    """Return the denominator of rational number X in lowest terms and positive."""
    return x[1]


t = rational(1, 3)
print_rational(t)
print_rational(add_rational(t, t))

# Functional realization
def pair(x, y):
    """Return a function that represents a pair."""

    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y

    return get

def select(p, i):
    """Return the element at index i of pair p."""
    return p(i)

p = pair(20, 14)
print(select(p, 0))

