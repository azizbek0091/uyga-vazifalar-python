import os; os.system('cls')

n = int(input("Sonni kiriting ==> "))
yigindi = 0

for i in range(1, n + 1):
    yigindi += i
    print("+".join(map(str, range(1, i + 1))) + f"={yigindi}")