import os; os.system("cls")

a = int(input("Raqamni kiriting ==> "))

if a % 3 == 0 and a % 5 == 0:
    print("FIZZBUZZ")
elif a % 3 == 0:
    print("FIZZ")
elif a % 5 == 0:
    print("BUZZ")