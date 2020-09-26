#Bai3
print()
print("Tính tổng các chữ số của số nguyên dương N")
n = int(input("Nhập số nguyên dương N: "))
tong = 0
while (n):
    if(n > 1000):
        print("N không được lớn hơn 1000, Nhập lại: ") 
        break
    if(n < 1000):
        while (n):
            tong = tong + n%10
            n = int(n/10)
print("Tổng của các chữ số của N là: ", tong)