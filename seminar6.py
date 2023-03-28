from math import sqrt, ceil
from datetime import datetime
def task39(arr1, arr2):
    """ task39 """
    return [i for i in arr1 if i not in arr2]


def task41(arr):
    """ task41 """
    return sum(1 for i in range(1, len(arr) - 1) if arr[i - 1] < arr[i] > arr[i + 1])


def task43(arr):
    """ task43 """
    tmp_arr = list(set(arr))
    return sum(arr.count(i) // 2 for i in tmp_arr)
    return sum(arr.count(i) - 1 for i in tmp_arr)


    """ task45 """
start_time = datetime.now()
def task45(k):
    def s_d(n): return 1+sum(i + n // i for i in range(2, ceil(sqrt(n))) if not n % i)
    return ((v1, v2) for v1 in range(1, k) if v1 < (v2 := s_d(v1)) < k and v1 == s_d(v2))



def main():
    """ run task 39"""
    # arr391 = [3, 1, 3, 4, 2, 4, 12]
    # arr392 = [4, 15, 43, 1, 15, 1]
    # print(*task39(arr391, arr392))
    # """ run task 41 """
    # arr41 = [1,5,1,5,1]
    # print(task41(arr41))
    # """ run task 43 """
    # arr43 = [1,2,3,2,3,2]
    # print(task43(arr43))
    """ run task 45 """
    k = 100000
    print(*task45(k))
    print(datetime.now() - start_time)

if __name__ == '__main__':
    main()
