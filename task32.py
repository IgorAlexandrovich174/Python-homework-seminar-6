'''Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]


Вывод: [1, 9, 13, 14, 19]
'''

def get_number(str):
    try:
        number = int(input(str))
    except ValueError:
        print('Введено не число')
        return get_number(str)
    return number

array = [-5, 9, 0, 3, -1, -2, 1,
         4, -2, 10, 2, 0, -9, 8, 10, -9,
         0, -5, -5, 7]
minimum = get_number('Введите минимальное значение диапазона: ')
maximum = get_number('Введите максимальное значение диапазона: ')
result = []
for i in range(len(array)):
    if minimum <= array[i] <= maximum:
        result.append(array[i])
print(result)