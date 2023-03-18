# 2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# Примеры/Тесты:
# 10 ->
# 1
# 2
# 4
# 8

number = int(input('Введите число N: '))
degree = 0
for k in range(number):
    degree = 2**k
    if degree > number: break
    print (2**k, end =', ')
    
    
    