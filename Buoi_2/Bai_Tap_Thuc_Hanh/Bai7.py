#Bai_7
print()
print("Tính tổng giá trị từ 1 đến N, riêng số 17 thì bỏ qua")
n = int(input("Nhập N: "))
print()
tong= 0
for i in range (1, n+1):
    if(i == 17):
        continue
    else:
        tong += i
        print(i, tong)
print()
print("==> Tổng là: ",tong)