import os; os.system("cls")

list = [1,2,3]
list1 = [61,228,9]

list_sortlangan = sorted(map(str, list), reverse=True)
list_sortlangan1 = sorted(map(str, list1), reverse=True)

yangi= ''
for i in list_sortlangan:
    yangi += i

yangi1 = ''
for i in list_sortlangan1:
    yangi1 += i

print(yangi)
print(yangi1)