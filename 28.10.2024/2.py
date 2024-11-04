import os; os.system("cls")

# juft sonlarni chiqarish

def juft(son):
    return son % 2 == 0

sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
juft_sonlar = list(filter(juft, sonlar))
print(juft_sonlar)

# 0 dan katta sonlarni chiqarish

def katta(son):
    return son > 0

sonlar = [-10, -5, 0, 5, 10, 15, -3]
katta_sonlar = list(filter(katta, sonlar))
print(katta_sonlar)
