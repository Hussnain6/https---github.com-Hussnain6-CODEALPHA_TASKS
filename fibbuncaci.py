print("Fibbunacci Series")
num=int(input("Enter a Number "))

def Fibbunacci(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return Fibbunacci(i-2)+ Fibbunacci(i-1)
    
for i in range(num):
    print(Fibbunacci(i),end=" ")