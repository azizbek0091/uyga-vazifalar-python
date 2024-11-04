import os; os.system("cls")

def uchramaydigan(a, b):
    new = list(set(a).symmetric_difference(set(b)))
    new.sort()
    return new

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("a = ", a)
print("b = ", b)

print("new = ", uchramaydigan(a, b))