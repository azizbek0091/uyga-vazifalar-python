import os; os.system("cls")

lst = [1, 2, 33, 5, 6, 7, 7]

son = int(input("Sonni kiriting ==> "))

index = []

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == son:
            index.append((i, j))

if index:
    for i in index:
        print(f"{i[0]}, {i[1]}")
else:
    print("Bunday yigindi yoq.")