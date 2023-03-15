# Задача 10: На столе лежат n монеток. Найти минимальное кол-во для перевернуть.
n = int(input())
m = [__import__('random').randint(0, 1) for _ in range(n)]
print(sum(m) if sum(m) < len(m) // 2 else len(m) - sum(m))

# Задача 12: Петя и Катя найти числа когда дана сумма и произведение
s, p = int(input()), int(input())
[print(i, s - i) for i in range(1, s // 2 + 1) if (s - i) * i == p]

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2 k)
n = int(input())
[print(2 ** i, end=' ') for i in range(n) if 2 ** i < n]

# Дополнительная задача. числа от 1 до 9 написаны в ряд,
# можно вставить + и - в любое место, нужно найти все комбинации, сумма которых = 100
s, d, summ, count = '123456789', {'0': '', '1': '+', '2': '-'}, 100, 0

for n in range(int('22222222', 3)):
    lst, rslt = [], ''

    if n == 0: lst.append('0')
    while n:
        lst.append(str(n % 3)); n //= 3

    num = f"{''.join(lst[::-1]):0>8}"

    for i, j in list(zip(s, num)): rslt += i + d[j]

    if eval(rslt + '9') == summ:
        print(f'{rslt + "9"}={summ}'); count += 1

print(f'Всего {count} выражений')
