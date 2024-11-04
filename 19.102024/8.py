import os; os.system("cls")

a = int(input("1-sonni kiriting ==> "))
b = int(input("2-sonni kiriting ==> "))
c = int(input("3-sonni kiriting ==> "))
d = int(input("4-sonni kiriting ==> "))

soni = 0

if a % 2 == 0:
    soni += 1

if b % 2 == 0:
    soni += 1

if c % 2 == 0:
    soni += 1

if d % 2 == 0:
    soni += 1

if soni >= 2:
    print(a,b,c,d)
else:
    print("0")