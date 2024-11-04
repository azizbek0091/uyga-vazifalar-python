import os; os.system("cls")

matn = "salom yoz. olam juda ham gozal. imtixon bolyapti."

belgi = ['.', ',']
yangi_matn = ""

for i in matn:
    if i not in belgi:
        yangi_matn += i

dict = yangi_matn.split()
a = matn.split(". ")
a = [soz.strip() for soz in a if soz]

print(dict)
print(a)