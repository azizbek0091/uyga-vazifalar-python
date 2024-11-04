import os; os.system("cls")

n = int(input("sonni kiriting ==> "))

sum = 0
for i in range(1, n+1):
    m = int('2' *i)
    sum += m

print("Yig'indisi ==> ", sum)