'''
 Tính tổng giá trị từ 1 đến n (n>13, n nhập từ bàn phím, xử lý điều kiện n>13), 
nếu chạy đến số 13 thì không chạy nữa (không cộng số 13) và xuất kết quả
Ví dụ: input: n = 20
 Output: S = 78
'''

def tinh_tong(n):
    tong = 0
    for i in range (1,n+1):
        if (i == 13 ):
            break
        else:
            tong += i
    return tong

print("Giá trị n chỉ được cộng đến thứ tự thứ 13")

if __name__ == "__main__":
    n = int(input("Nhập N = "))
    print("Tổng giá trị từ 1 đến ",n," là: ",tinh_tong(n))