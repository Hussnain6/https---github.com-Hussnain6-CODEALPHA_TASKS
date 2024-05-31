print("Fibbunacci Series")
num=int(input("Enter a number "))

def fibbunacci(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fibbunacci(i-2)+ fibbunacci(i-1)
    
for i in range(num):
    print(fibbunacci(i),end=" ")