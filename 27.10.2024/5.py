import os; os.system("cls")

list = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

def belgi_bilan_boshlangan(list, i):
    return [j for j in list if j.startswith(i)]

print("a harfi bilan boshlanadiganlar ==> ")
print(belgi_bilan_boshlangan(list, 'a'))

print("d harfi bilan boshlanadiganlar ==> ")
print(belgi_bilan_boshlangan(list, 'd'))

print("w harfi bilan boshlanadiganlar ==> ")
print(belgi_bilan_boshlangan(list, 'w'))