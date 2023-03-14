# Задача 10: На столе лежат n монеток. Найти минимальное кол-во для перевернуть.
n = [__import__('random').randint(0, 1) for _ in range(15)]
print(n.count(0) if n.count(0) < n.count(1) else n.count(1))
# альтернатива
print(sum(n) if sum(n) < len(n)//2 else len(n) - sum(n))

# Задача 12: Петя и Катя найти числа когда дана сумма и произведение
s, p = int(input()), int(input())
[print(i, s-i) for i in range(1, s//2+1) if (s-i) * i == p]

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2 k)
n = int(input())
[print(2**i, end=' ') for i in range(n) if 2**i < n]
