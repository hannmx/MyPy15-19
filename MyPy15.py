#Вычислить число с заданной точностью d
#Решение с использованием ряда Лейбница

import math
def calc_pi(eps):
    n = 2
    pi = 4 * [1, -1/3]
    diff = 1
    while diff > eps:
        pi.append(4 * (-1)**n / (2 * n + 1))
        diff = abs(sum(pi[:-1]) - sum(pi[:-2]))
        n += 1
    return math.floor(sum(pi) * int(1/eps)) * eps
eps = float(input('Введите точность для вычисления числа pi: '))
print(f"Полученное число: {calc_pi(eps)}")