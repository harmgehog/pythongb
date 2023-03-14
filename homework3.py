# # Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
# # в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны
# # N целых чисел Ai. Последняя строка содержит число X.   5   1 2 3 4 5   3   ->   1
Ai, X = [int(input()) for _ in range(int(input()))], int(input())
print(Ai.count(X))

# # Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь
# # в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны
# # N целых чисел Ai. Последняя строка содержит число X.    5   1 2 3 4 5   6 -> 5
Ai, X = [int(input()) for _ in range(int(input()))], int(input())
print(min(Ai, key=lambda n: abs(n - X)))

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским
# алфавитом очки распределяются так: Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
dictionary = {'aeioulnstr': 1, 'dg': 2, 'bcmp': 3, 'fhvwy': 4, 'k': 5, 'jx': 8, 'qz': 10,
              'авеинорст': 1, 'дклмпу': 2, 'бгёья': 3, 'йы': 4, 'жзхцч': 5, 'шэю': 8, 'фщъ': 10}
summ = 0
for x in input():
    for key in dictionary:
        if x.lower() in key:
            summ += dictionary.get(key)
print(summ)
