P = 1
N = 5
for i in range(1, N + 1):
    print("value product of number on previous step:", P)
    print("current step value: ", i)
    P = P * i
    print("value product of number after multiplication:", P)
    print("- - -")
print("End of cycle")
print()
print("Answer: product of numbers is", P)
