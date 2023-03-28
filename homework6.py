
def task30(a1, d, n):
    """ task30
    Заполните массив элементами арифметической прогрессии. """
    return (a1 + i * d for i in range(n))


def task32(lst, minn, maxn):
    """ task32 Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону"""
    return [i for i in range(len(lst)) if minn <= lst[i] <= maxn]


def main():
    """ run task 30"""
    a1, d, n = (int(input()) for i in range(3))
    print(*task30(a1, d, n))
    """ run task32 """
    lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    minn, maxn = (int(input()) for i in range(2))
    print(*task32(lst, minn, maxn))

if __name__ == '__main__':
    main()