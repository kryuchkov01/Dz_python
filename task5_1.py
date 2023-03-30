# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16


number1 = 2
number2 = 4

def degree(num, extent):
    if extent == 0:
        return 1
    elif extent == 1:
        return num
    else:
        return (num*degree(num, extent-1))


print(degree(number1, number2))