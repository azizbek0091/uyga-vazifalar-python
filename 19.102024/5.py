import os; os.system("cls")

a = int(input("1-sonni kiriting ==> "))
b = int(input("2-sonni kiriting ==> "))
c = int(input("3-sonni kiriting ==> "))
d = int(input("4-sonni kiriting ==> "))

juft = 0
toq = 0

if a % 2 == 0:
    juft += a
else :
    toq += a

if b % 2 == 0:
    juft += b
else :
    toq += c

if c % 2 == 0:
    juft += c
else :
    toq += c

if d % 2 == 0:
    juft += d
else :
    toq += d

toq = toq * 3
juft = juft + 10

print("Toqlarini 3 ga kopaytmasi ==> ", toq)
print("Juftlarini 10 ga yig'indisi ==> ", juft)