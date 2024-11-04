import os; os.system("cls")

def bittadan(numbers):
    result = [i for i in numbers if numbers.count(i) > 1]
    return result

N = int(input("Elementlar sonini kiriting ==> "))
numbers = list(map(int, input("N ta sonni kirting ==> ").split()))

print("sonlar =", bittadan(numbers))