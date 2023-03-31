'''Задача 30: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Ввод: 7 2 5

Вывод: 7 9 11 13 15
'''
import re
def arithmeticProgressionArray() :
    flag = False
    array = []
    temp = 0
    while(not flag) :
        inputValues = input("Введите через пробел первый элемент массива, затем разность, затем количество элементов: ")

        inputValuesSplit = re.split(r'[;,.!\s]',inputValues)
        

        if len(inputValuesSplit) < 3 or len(inputValuesSplit) > 3 :
            print(f"Вводите не более 3 значений!\n  1.Первый элемент массива \n  2.Разность \n  3.Размер массива" )
        else :
            temp = int(inputValuesSplit[0])
            array.append(temp)
            while(len(array) < int(inputValuesSplit[2])) :
                temp += int(inputValuesSplit[1])
                array.append(temp)

            flag = True
    print(array)

        
arithmeticProgressionArray()