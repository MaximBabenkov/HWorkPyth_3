#  Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#  Пример:

# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibon_rec(numb: int):
    if (numb <= 1):
        return numb
    else:
        return fibon_rec(numb - 1) + fibon_rec(numb - 2)

def fibon_rec_neg(numb: int):
    if numb == -1:
        return 1
    elif numb == -2:
        return -1
    else:
        return fibon_rec_neg(numb + 2) - fibon_rec_neg(numb + 1)

def fibon_list(number: int):
    list = []

    for i in range(-number, 0):
        list.append(fibon_rec_neg(i))

    for i in range(0, number+1):
        list.append(fibon_rec(i))

    return list

number = int(input('Enter your number: '))
my_list = fibon_list(number)
print(f'Your Fibonacci sequence:\n{my_list}')