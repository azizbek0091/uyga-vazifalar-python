import os; os.system('cls')

N = int(input("Sonni kirting ==> "))

royxat = []
lugat = []

print("sonlarni kiriting ==> ")

for i in range(N):
    num = int(input())
    royxat.append(num)
    if num in lugat:
        lugat[num] += 1
    else:
        lugat[num] = 1

print("2 marta va undan kop takrorlanagan sonlar ==> ")
for num, cnt in lugat.items():
    if i >= 2:
        print(num)