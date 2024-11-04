import os; os.system("cls")

list = [[1, "Jean Castro", "V"], [2, "Lule Powell", "V"], [3, "Brian Howell", "VI"], [4, "Lynne Foster", "VI"], [5, "Zachary Simon", "VII"]]

dictionary = {i[0]: [i[1], i[2]] for i in list}

print(dictionary)