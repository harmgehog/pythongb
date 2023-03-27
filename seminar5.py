# task 31
def fib(n):
    return 1 if n<2 else fib(n-1) + fib(n-2)


print(f'Это число: {fib(int(input("Введите порядковый номер члена ряда фибоначчи: ")))}')


# task 33
def journal(fin):
    if len(fin) > 0:
        s = fin.pop()
        return str(journal(fin)) + str(6-s if s>3 else s) + ' '
    return ''


print(f'Мама, я починил: {journal([1, 3, 3, 5, 4])}')


# task 37
def reversa(a):
    s = input()
    if a: reversa(a-1)
    print(s, end=' ')


n = int(input())
reversa(n-1)



