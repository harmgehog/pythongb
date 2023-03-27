def summ(a, b): return summ(a+1, b-1) if b else a


def main():
    # task 26 анонимкой рекурсию
    mult = lambda x, n: x * mult(x, n - 1) if n else 1
    print(mult(3, 5))
    # task 28 А следующую задачу по всем канонам
    print(summ(5, 2))


if __name__ == '__main__':
    main()
