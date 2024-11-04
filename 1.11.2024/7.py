import os; os.system('cls')

file = open("7-misol.txt", "rt")

raqamlar = file.read()

file.close()
yig = 0

for i in raqamlar:
    if i.isdigit():
        yig = yig + int(i)
        print(i, end="  ")
print("\nsonlarni yigindisi ==> ", yig)