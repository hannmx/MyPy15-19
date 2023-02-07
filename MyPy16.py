# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

N = int(input("Введите число: "))
first_num = 2 
listN = []
first_N = N
while first_num <= N:
    if N % first_num == 0:
        listN.append(first_num)
        N //= first_num
        first_num = 2
    else:
        first_num += 1
print(f"Простые множители числа {first_N} приведены в списке: {listN}")