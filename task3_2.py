# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному 
# числу X. Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10

list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
numb = int(input('Введите число X: '))

min_diff = abs(list[0] - numb)
numb_found = list[0]

for i in range(len(list)-1):
    if abs(list[i] - numb) < min_diff:
        min_diff = abs(list[i] - numb)
        numb_found = list[i]

print(numb_found)

    

    