soz = input("So'zni kiriting: ")
harf = input("Harfni kiriting: ")

natija = ""
for i in soz:
    if i == harf:
        natija += i.upper()
    else:
        natija += i

print(natija)