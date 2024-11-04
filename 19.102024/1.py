import os; os.system("cls")

a = int(input("1-sonni kiriting ==> "))
b = int(input("2-sonni kiriting ==> "))
c = int(input("3-sonni kiriting ==> "))
d = int(input("4-sonni kiriting ==> "))
e = int(input("5-sonni kiriting ==> "))
f = int(input("6-sonni kiriting ==> "))

juft = 0
toq = 0

if a % 2 == 0:
    juft += 1
else :
    toq += 1

if b % 2 == 0:
    juft += 1
else :
    toq += 1

if c % 2 == 0:
    juft += 1
else :
    toq += 1

if d % 2 == 0:
    juft += 1
else :
    toq += 1

if e % 2 == 0:
    juft += 1
else :
    toq += 1

if f % 2 == 0:
    juft += 1
else :
    toq += 1

print("Juft sonlar soni ==> ", juft)
print("Toq sonlar soni ==> ", toq)