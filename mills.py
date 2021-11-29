#!/usr/bin/python3
import math
import sys


def combinations(n, k):
    n = int(n)
    k = int(k)
    if k > n:
        return 0
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def mills(V, v, n, k=None):
    # V - Сколько добавили ошибок
    # v - Сколько нашли из добавленных
    # n - сколько наших ошибок было найдено
    # k - количество предполагаемых ошибок
    N = V * n / v
    if k is None:
        k = N
    if n > k:
        return N, 1
    else:
        return N, V / (V + k + 1)


def mills1(V, v, n, k=None):
    # V - Сколько добавили ошибок
    # v - Сколько нашли из добавленных
    # n - сколько наших ошибок было найдено
    # k - количество предполагаемых ошибок
    N = V * n / v
    if k is None:
        k = N
    if n > k:
        return N, 1
    else:
        return N, combinations(V, v - 1) / combinations(V + k + 1, k + v)


_, n, _ = map(float, sys.stdin.readline().split())
v = int(sys.argv[1])
# v - сколько добавили
# n - сколько всего ошибок
N, C = mills(v, n - (n - v), n - v)
print("Количество ошибок в программе:", N)
print("Отлаженность программы:", C)
N, C = mills1(v, n - (n - v), n - v)
print("Количество ошибок в программе:", N)
print("Отлаженность программы:", C)
# N, C = mills(10, 10, 0, 0)
# print("Количество ошибок в программе:", N)
# print("Отлаженность программы:", C)
#
# N, C = mills1(10, 6, 4, 6)
# print("Количество ошибок в программе:", N)
# print("Отлаженность программы:", C)