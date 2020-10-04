#Bài 2: Tính n!
print()
print("Bài 2: Tính n!")
n = int(input("Nhập N: "))
def tinhgiaithua(n):
    if n == 0:
        return 1
    return n * tinhgiaithua(n - 1)
print("Giai thừa của",n,"là: ",tinhgiaithua(n))