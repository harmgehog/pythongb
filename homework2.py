# Задача No9. сделать факториал через while

n, x = int(input('Введите число: ')), 1
while n > 0:
    x *= n
    n -= 1

print(x)

# Задача 10: На столе лежат n монеток. Найти минимальное кол-во для перевернуть.

n = [__import__('random').randint(0, 1) for _ in range(15)]
print(n.count(0) if n.count(0) < n.count(1) else n.count(1))
print(sum(n) if sum(n) < len(n)//2 else len(n) - sum(n))

# Задача No11. Дано A > 1. Определите число Фибоначчи φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

n, fprev, fnext, counter = int(input()), 0, 1, 1

while fnext <= n:
    if fnext == n:
        print(counter)
        break
    fprev, fnext = fnext, fprev + fnext
    counter += 1
else:
    print(-1)

# Задача 12: Петя и Катя найти числа когда дана сумма и произведение

s, p = int(input()), int(input())

for i in range(1, s):
    if (s-i) * i == p:
        print(i, s-i)
        break

# Задача No13. Количество дней > 0 градусов C. N – (1 ≤ N ≤ 100). T от –50 до 50

cnt, last_cnt, n = 0, 0, int(input())

for i in range(1, n+1):
    temp = int(input())
    if temp > 0:
        cnt += 1
    else: cnt = 0
    if cnt > last_cnt: last_cnt = cnt

print(last_cnt)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2 k)

n = int(input())

[print(2**i, end=' ') for i in range(n) if 2**i < n]

# Задача No15. Из арбузов найти MAX & MIN

n = [int(input()) for _ in range(int(input()))]
print(min(n), max(n))

indexofmax = [i for i, val in enumerate(n) if val == max(n)]

