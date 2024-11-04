import os; os.system("cls")

raqamlar = [123,456,789,852,12,42,61,369]

print(*raqamlar)

list = [i for i in raqamlar if i % 2 == 0]

print(*list)