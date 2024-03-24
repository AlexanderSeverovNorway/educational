string = input("Введите числа через пробел:")
list_of_strings = string.split()
list_of_numbers = list(map(int, list_of_strings))
print(sum(list_of_numbers[::3]))
