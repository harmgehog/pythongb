def lyrics_or_not(s):
    """ task 34 Так как винни пух знает только одну гласную букву, то он нам облегчает задачу"""
    for i in 'оеиуыюэя':
        s = s.replace(i, 'а')
    return ['Пам парам', 'Парам пам-пам'][len(set([i.count('а') for i in s])) < 2]
    # return ['Пам парам', 'Парам пам-пам'][len(set(map(lambda x: len([i for i in x if i in 'ауоияюэ']), s.split()))) < 2]
    # print(['Пам парам', 'Парам пам-пам'][len(set(map(lambda x: x.count('a'), s.split())))<2])


def print_operation_table(f, rs=6, cs=6):
    """ task 36 """
    [print(*[f(r, c) for r in range(1, rs+1)], sep='\t') for c in range(1, cs+1)]


def main():
    """ run task 34"""
    print(lyrics_or_not(input()))
    """ run task 36"""
    print_operation_table(lambda x, y: x * y)


if __name__ == '__main__':
    main()
