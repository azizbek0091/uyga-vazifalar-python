import os; os.system("cls")

list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9 , 7, 1]

nol_bolmagan = [i for i in list if i != 0]
nol_bolgan = [i for i in list if i == 0]

yangi_list = nol_bolmagan + nol_bolgan

print(yangi_list)