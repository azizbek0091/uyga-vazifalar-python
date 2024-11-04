import os; os.system('cls')

file1 = open(str(input("fayl nomini kiritng ==> ")), "w")
file1.write(str(7519318749))

file1.close()

file2 = open("new1.txt", "w")

file3 = open("new2.txt", "w")

file1 = open(str(input("qaysi fayl ==> ")), "rt")

raqam = file1.read()

raqamlar = (sorted(raqam, reverse=True))
file2.write(str(raqamlar))
raqamlar1 = sorted(raqam)
file3.write(str(raqamlar1))

print("bajarildi")

file1.close()
file2.close()
file3.close()