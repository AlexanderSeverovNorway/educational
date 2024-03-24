a = input("Введите первую строку: ").split()
b = input("Введите вторую строку: ").split()
a_set, b_set = set(a), set(b)  # используем множественное присваивание
a_b = a_set.symmetric_difference(b_set)
a_b = list(map(int, a_b))
a_b = sorted(a_b)
print(a_b)
