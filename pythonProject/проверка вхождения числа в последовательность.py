print(list(str(123456789)))

print(list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])))

list_digit = list(map(int, list(str(123456789))))
print(5 in list_digit)
