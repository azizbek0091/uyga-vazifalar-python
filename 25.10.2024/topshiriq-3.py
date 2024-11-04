import os; os.system("cls")

dict1 = {1:'ABC', 2:'DEF', 3:'GHI', 4:'JKL', 5:'MNO'}

keys = list(dict1.keys())

for i in range(1, len(keys), 2):
    dict1[keys[1]], dict1[keys[i-1]] = dict1[keys[i-1]], dict1[keys[i]] 

print(dict1)