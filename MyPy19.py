
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('first_poly.txt', 'w', encoding='utf-8') as file:
    file.write('5*x^3 + 2*x^2 + 19*x^4')
with open('second_poly.txt', 'w', encoding='utf-8') as file:
    file.write('8*x^9 + 11*x^7 + 7*x^3')

with open('first_poly.txt','r') as file:
    first_poly = file.__next__()


with open('second_poly.txt','r') as file:
    second_poly = file.__next__()

print(first_poly)
poly_sum = first_poly + ' + ' + second_poly
print('Сумма двух многочленов равна: ')
print(f'{first_poly} + {second_poly} = {poly_sum}')

with open('poly_sum.txt', 'w', encoding='utf-8') as file:
    print('Sum\n')
    file.write(f'{poly_sum}')