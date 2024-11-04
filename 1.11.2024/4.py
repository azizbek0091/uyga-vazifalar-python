import os; os.system('cls')

file = open("4-misol.txt", "rt")

gap = file.readline()
print(gap)

qancha = 0

for i in gap:
    if (i.isdigit()):
        qancha += 1

print(qancha,"ta")

file.close()