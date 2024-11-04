import os; os.system('cls')

son = int(input("Sonni kiriting: "))

ikkilik_sanoq_sistema = bin(son)[2:] 

nollar_soni_xisoblash = ikkilik_sanoq_sistema.count('0')

print(f"{son} - Ikkilik sanoq sistemasida ==> ", nollar_soni_xisoblash)