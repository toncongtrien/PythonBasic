#Bài 4: Tính tổng các chữ số lẻ
print()
print("Bài 4: Tính tổng các chữ số lẻ")
n = int(input("Nhập N: "))
def tong(n):
    s = 0
    for i in range (0,n+1):
        if(i % 2 != 0):
            s += i
    return s
print("Tổng các chữ số lẻ là: ",tong(n))