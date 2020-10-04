#Bài 3: Tính tổng 1^3+2^3+..n^3
print()
print("Bài 3: Tính tổng 1^3+2^3+..n^3")
n = int(input("Nhập N: "))
s = 0
for i in range (1, n+1):
    s = s + pow(i,3)
    print(s)
