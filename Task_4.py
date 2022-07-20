# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
 
def get_bin_numb(numb: int):
    result = " "
    while numb > 0:
        bit = numb % 2
        result = str(bit) + result
        numb = numb // 2
    return result

decim_numb = int(input('Enter your number: '))
binary_numb = get_bin_numb(decim_numb)
print('Your binary number:', binary_numb)
