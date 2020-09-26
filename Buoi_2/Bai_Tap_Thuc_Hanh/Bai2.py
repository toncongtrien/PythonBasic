#Bai_2
print()
print("Tính tổng các số từ 1 đến N")
sum = 0
n = int (input("Nhập N: "))
print()
while not n >= 0:
    n = int (input("N phải lớn hơn 0. Nhập lại: "))
for i in range (1, n+1):
    sum += i
    print(i)
print()
print("==> Tổng các số từ 1 đến N: ",sum)