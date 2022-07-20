#  Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#  Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def create_list(size: int, min_value: int, max_value: int):
    from random import randint
    new_list = []
    for i in range(size):
        new_list.append(randint(min_value, max_value))
    return new_list

def summ_odd_pos(list: list):
    summ = 0
    for i in range(len(list)):
        if i % 2 != 0:
            summ += list[i]
    return summ

amount = int(input('Enter amount of items in your list: '))
minn = int(input('Enter the minimum value in your list: '))
maxx = int(input('Enter the maximum value in your list: '))
my_list = create_list(amount, minn, maxx)
print('Your list:', my_list)
my_summ = summ_odd_pos(my_list)
print('The sum of items with odd indexes:', my_summ)

