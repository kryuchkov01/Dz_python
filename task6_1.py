# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
#  разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го 
#  члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

el1, diff, number_el = [int(el) for el in input("Input 1st element, difference and number of el: ").split()]


def progression (el1, diff, number_el):
    return [el1 + n*diff for n in range(number_el)]

print(progression(el1, diff, number_el))



