# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности

first_lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {first_lst}")
new_lst = []
[new_lst.append(i) for i in first_lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")