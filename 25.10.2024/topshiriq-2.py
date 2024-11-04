import os; os.system("cls")

matn = input("Matnni kiriting ==> ")

dictionary = {}

for i in matn:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print(dictionary)