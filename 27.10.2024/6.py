import os; os.system("cls")

def birlashtir(list1, list2):
    list3 = []

    for i in range(max(len(list1), len(list2))):
        if i < len(list1):
            list3.append(list1[i])
        if i < len(list2):
            list3.append(list2[i])
    
    return list3

print(birlashtir([1,2,3], [11,22,33]))
print(birlashtir([1,2,3,4,5], [11,22,33]))
print(birlashtir([1,2], [11,22,33,44,55,]))