#Bai_6
print()
print("Tính tổng giá trị từ 1 đến N, nếu chạy đến số 13 thì không chạy nữa và xuất kết quả")
n = int(input("Nhập N: "))
print()
tong = 0
for i in range (1, n+1):
    if (i == 13 ):
        break
    else:
        tong += i
        print(i, tong)
print()
print("==> Tổng giá trị là: ",tong)