import os; os.system('cls')

matn = input("Matnni kiriting ==> ")

words = matn.split()

sortlangan = sorted(words, key=lambda x: x[0].lower())

print(" ".join(sortlangan))