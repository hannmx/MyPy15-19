# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k
import random
k = int(input('Введите натуральную степень многочлена: '))

#заполнение списка коэффициентов многочлена в зависимости от степени
coeff_list = []     
for i in range(k + 1):
     coeff_list.append(random.randint(0,3))
print(coeff_list)

f = open('18Python.txt', 'w')
f.write(f'A polynomial of {k} degrees: ')
while k > 0:
    for i in range(len(coeff_list)):
        if coeff_list[i] == 0:
            print(end='', file=f)
        elif k == 0:
            print(str(coeff_list[i]), end= '', file=f)
        elif k == 1 and coeff_list[i + 1] == 0:
            print(str(coeff_list[i]) + 'x', end='', file=f)
        elif k == 1:
            if coeff_list[i] == 1:
                print('x + ', end='', file=f)
            else:
                print(str(coeff_list[i]) + 'x + ', end='', file=f)
        else:
            if coeff_list[i] == 1:
                print('x^' + str(k) + ' + ', end='', file=f)
            else:
                print(str(coeff_list[i]) + 'x^' + str(k) + ' + ', end='', file=f) 
        k -= 1
print(' = 0', file=f)
f.close()  
