import os; os.system("cls")

list = [1,2,3,4]
string = input("Stringni kiriting ==> ")

yangi_list = [string + str(i) for i in list]
print(yangi_list)