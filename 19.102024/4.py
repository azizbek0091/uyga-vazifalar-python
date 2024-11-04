import os; os.system("cls")

a = int(input("1-sonni kiriting ==> "))
b = int(input("2-sonni kiriting ==> "))
c = int(input("3-sonni kiriting ==> "))

sum = 0

if a % 2 == 0:
    sum += a
if b % 2 == 0:
    sum += b
if c % 2 == 0:
    sum += c

print("Juft sonlar yig'indisi", sum)