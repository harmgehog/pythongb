def same_by(char, obj):
    """ task 51 """
    return len(set(map(char, obj))) < 2


def find_farthest_orbit(orbits):
    return max({a * b: (a, b) for a, b in orbits if a != b}.items())


def main():
    # """ run task 47"""
    # values = [1, 23, 42, 'asdfg']
    # trans_val = list(map(lambda x: x, values))
    # print('ok' if values == trans_val else 'fail')
    #
    """ run task 49 """
    orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
    print(*find_farthest_orbit(orbits)[1])
    #
    # """ run task 51 """
    # values = [0, 2, 10, 6]
    # print('same' if same_by(lambda x: x % 2, values) else 'different')


if __name__ == '__main__':
    main()
