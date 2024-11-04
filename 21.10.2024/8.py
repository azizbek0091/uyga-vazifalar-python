n = int(input("n ni kiriting: "))

yigindi = 0
raqam = 0

for i in range(n):
    raqam = raqam * 10 + 2  
    yigindi += raqam
    
print("Yig'indi:", yigindi)