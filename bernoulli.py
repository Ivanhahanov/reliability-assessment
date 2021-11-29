#!/usr/bin/python3
import math
import sys


def bernoulli(p, n, k):
    c = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return c * p ** k * (1 - p) ** (n - k)


n, k1, p = map(float, sys.stdin.readline().split())
k = int(sys.argv[1])

print("Количество запусков:", int(n))
print("Процент неудач:", p)
print("Ожидаемое количество запусков:", k)
b = bernoulli(p, n, k)
r = (n - k1) / n
print()
print(f"Вероятность из {int(n)} запусков {k} приведут к ошибкам: ", round(b, 4))
print("Надежность программы:", round(r, 4))
