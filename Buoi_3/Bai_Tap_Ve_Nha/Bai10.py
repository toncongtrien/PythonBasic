'''
Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
        Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
'''
import math
print()
n = int(input("Nhập N: "))
def tongcacsole(n):
    s = 0
    count = 0
    while (n):
        s =  n % 10
        if(s % 2 != 0):
            count = count + 1
        n = int(n / 10)
    print("Số lượng chữ số lẻ của N là: ",count)
tongcacsole(n)