#Bài 5: Tính tổng các chữ số chẵn
print()
print("Bài 5: Tính tổng các chữ số chẵn")
n = int(input("Nhập N: "))
def tong(n):
    s = 0 
    for i in range (0, n+1):
        if(i % 2 == 0):
            s += i
    return s
print("Tổng các số chẵn là: ", tong(n))
