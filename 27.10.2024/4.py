import os; os.system("cls")

list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

yangi_list = []
for i in list:
    if i not in yangi_list:
        yangi_list.append(i)

print(yangi_list)