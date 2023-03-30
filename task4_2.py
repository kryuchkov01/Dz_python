# 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены 
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста 
# и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом. На входе задано количество ягод на каждом кусте. Не обязательно вводить их с 
# клавиатуры, можно задать непосредственно в коде программы
# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7
# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1

input1 = [1, 2, 3, 4, 5, 6, 7, 8]
count = []
max_sum = 0

for i in range(len(input1)-1):
    sum = 0
    sum = int(input1[i] + input1[i-1] + input1[i+1])
    if sum > max_sum:
        max_sum = sum
        number = input1[i]
  
print(f"Макс. кол-во ягод {max_sum}, собрано для куста {number}")



