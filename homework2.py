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
# from datetime import datetime
#
# start_time = datetime.now()
y = 0
for a in '+-*/ ':
    for b in '+-*/ ':
        for c in '+-*/ ':
            for d in '+-*/ ':
                for e in '+-*/ ':
                    for f in '+-*/ ':
                        for j in '+-*/ ':
                            for g in '+-*/ ':
                                phrase = '1' + a + '2' + b + '3' + c + '4' + d + '5' + e + '6' + f + '7' + j + '8' + g + '9'
                                phrase = phrase.replace(' ', '')
                                if eval(phrase) == 100:
                                    print(phrase, '= 100')
                                    y += 1
print(y)
# print(datetime.now() - start_time)

# вторая дополнительная задача
n = [91, 228, 9]
[print(x[:-4], end='') for x in sorted([str(i)+'9999' for i in n])[::-1]]
