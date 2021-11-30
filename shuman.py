import math
from scipy import integrate

t = 0
C = 0.7
N = 0
errors = range(9, 1, -1)


def risk():
    return C * (N - 1)


def shuman(t):
    return math.exp(-risk() * t)


def mtfb():
    return integrate.quad(shuman, 0, float('inf'))


if __name__ == '__main__':
    for i, n in enumerate(errors):
        N = n
        print(f"t={i} N={n} R(t)={round(shuman(i), 4)}")
        print("Среднее время между отказами:", round(mtfb()[0], 4))