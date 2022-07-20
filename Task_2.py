#   Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#    Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def create_list(size: int, min_value: int, max_value: int):
    from random import randint
    new_list = []
    for i in range(size):
        new_list.append(randint(min_value, max_value))
    return new_list

def prod_pairs_numb(lst: list):
    prod_pairs = []
    i_start = 0
    i_end = len(lst)-1
    prod = 0
    while i_start < i_end:
        prod = lst[i_start] * lst[i_end]
        prod_pairs.append(prod)
        i_start += 1
        i_end -= 1
    return prod_pairs

amount = int(input('Enter amount of items in your list: '))
minn = int(input('Enter the minimum value in your list: '))
maxx = int(input('Enter the maximum value in your list: '))
my_list = create_list(amount, minn, maxx)
print('Your list:', my_list)
my_prods = prod_pairs_numb(my_list)
print('The produсts of pairs of numbers:', my_prods)