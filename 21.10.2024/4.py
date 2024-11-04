import os; os.system('cls')

sentence = input("Gapni kiriting: ")

words = sentence.split()


for i in range(len(words)):
    if len(words[i]) % 2 != 0:
        words[i] = words[i][::-1] 

print(" ".join(words))