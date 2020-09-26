#Bai_3
print()
print("Tính tổng các số chẵn từ 1 đến N")
n= int(input('Nhập N = '))
print()
chan = 0
for i in range (0, n+1):
    if( i % 2 == 0):
        chan += i
        print ("Các số chẵn bao gồm: ",i)  
    else:
        print("...")
print()
print("==> Tổng các số chẵn là: ",chan)