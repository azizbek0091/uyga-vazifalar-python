import os; os.system("cls")

# kvadrat sonlar

def kvadrat(son):
    return son ** 2

sonlar = [1, 2, 3, 4, 5]
kvadrat_sonlar = list(map(kvadrat, sonlar))
print(kvadrat_sonlar)

# Katta harfga almashtirish

def katta_harf(soz):
    return soz.upper()

sozlar = ['salom', 'dunyo', 'python']
katta_harf_sozlar = list(map(katta_harf, sozlar))
print(katta_harf_sozlar)