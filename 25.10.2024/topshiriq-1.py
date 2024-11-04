import os; os.system("cls")

list1 = ['S001', 'S002', 'S003', 'S004']
list2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list3 = [85,98,89,92]

yangi_list = [{list1[i]: {list2[i]: list3[i]}} for i in range(len(list1))]

print(yangi_list)