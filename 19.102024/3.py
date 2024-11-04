import os; os.system("cls")

a = int(input("1-sonni kiriting ==> "))
b = int(input("2-sonni kiriting ==> "))
c = int(input("3-sonni kiriting ==> "))

if a < b < c:
    print("O'rtacha son ==> ", b)
elif b < a < c:
    print("O'rtacha son ==> ", a)
else :
    print("O'rtacha son ==> ", c)