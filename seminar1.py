# задача 1
print((m := int(input())) // (n := int(input())) + (m % n > 0))
print((m + n - 1) // n)  # альтернатива
# задача 3 парты 20,21,22 map(int, input().split())
rslt = sum([(i := int(input())) + i % 2 for _ in "ABC"])
rslt = rslt // 2 + rslt % 2
print(f'Количество парт: {rslt} шт.')

a, b, c = int(input()), int(input()), int(input())
result = (a + a % 2 + b + b % 2 + c + c % 2) // 2
print(f'Количество парт: {result} шт.')

# задача 5
(lambda i, j: print(['без дополнительной информации это сделать невозможно', i + j - 1][i != j]))(3, 4)

# задача 7 в соответствии с григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
''' ПЕРВОЕ РЕШЕНИЕ'''
a = int(input('Введите год: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('YES')
else:
    print('NO')

''' ВТОРОЕ РЕШЕНИЕ'''
print(['NO', 'YES'][(a:=int(input('Год: '))%4==0) and a%100!=0 or a%4==0])
