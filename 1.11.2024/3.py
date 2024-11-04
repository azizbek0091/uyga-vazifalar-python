import os; os.system('cls')

file = open("3-misol.txt", "rt")

gap = file.readline()
print(gap)

qancha = 0

for i in gap:
    if (i.isalpha()):
        qancha += 1

print(qancha,"ta")
file.close()