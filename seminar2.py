# # Задача No9. Посчитать факториал через while
# n, x = int(input('Введите число: ')), 1
# while n > 0:
#     x *= n; n -= 1
# print(x)

# # Задача No11. Дано A > 1. Определите число Фибоначчи φ(n)=A. Если А не
# # является числом Фибоначчи, выведите число -1.
# n, fprev, fnext, counter = int(input()), 0, 1, 1
#
# while fnext <= n:
#     if fnext == n:
#         print(counter)
#         break
#     fprev, fnext = fnext, fprev + fnext
#     counter += 1
# else:
#     print(-1)

# # Задача No13. Количество дней > 0 градусов C. N – (1 ≤ N ≤ 100). T от –50 до 50
# cnt, max_cnt, n = 0, 0, int(input())
# for i in range(n):
#     temp = int(input())
#     if temp > 0:
#         cnt += 1
#     else:
#         cnt = 0
#     if cnt > max_cnt: max_cnt = cnt
# print(max_cnt)

# Задача No15. Из арбузов найти MAX & MIN

# cnt = [int(input()) for _ in range(int(input()))]
#
# print(min(cnt), max(cnt))
#
# indexofmax = [i for i, wm in enumerate(cnt) if wm == max(cnt)]
