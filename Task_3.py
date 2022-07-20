#  Задайте список из вещественных чисел. Напишите программу, которая найдёт
#  разницу между максимальным и минимальным значением дробной части элементов.

#     Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def create_list_real_numbs(size: int):
    import random
    new_list = []
    for i in range(size):
        real_numb = round(random.random()*10, 2)
        new_list.append(real_numb)
    return new_list

def list_fract_parts(real_numbs: list):
    list_fract_parts = []
    fract_part = 0
    for i in range(len(real_numbs)):
        if real_numbs[i] < 0:
            fract_part = int(real_numbs[i]) - real_numbs[i]
        else:
            fract_part = real_numbs[i] - int(real_numbs[i])
        list_fract_parts.append(round(fract_part, 2))
    return list_fract_parts
    
def find_minn_maxx(list_in: list):
    maxx = 0.0
    minn = 1.0
    for i in range(len(list_in)):
        if list_in[i] > maxx:
             maxx = list_in[i]
        if list_in[i] < minn:
             minn = list_in[i]
        
    return maxx, minn

amount = int(input('Enter amount of items in your list: '))
my_list = create_list_real_numbs(amount)
print('Your list:', my_list)
fract_list = list_fract_parts(my_list)
elem_max, elem_min = find_minn_maxx(fract_list)
print('The maximal fractal part:', elem_max)
print('The minimal fractal part:', elem_min)
result = elem_max - elem_min
print('The diffirence:', round(result, 2))