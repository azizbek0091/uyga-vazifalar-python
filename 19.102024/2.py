import os; os.system("cls")

a = int(input("1-sonni kiriting ==> "))
b = int(input("2-sonni kiriting ==> "))
c = int(input("3-sonni kiriting ==> "))

if a > b and a > c:
    print("Katta son ==> ", a)
elif b > a and b > c:
    print("Katta son ==> ", b)
else:
    print("Katta son ==> ", c)