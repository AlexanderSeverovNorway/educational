def linear_solve(a, b):
    if a:
        return b/a
    elif not a and not b:
        return "Бесконечное число корней"
    else:
        return "Нет корней"
print(linear_solve(0, 1))
