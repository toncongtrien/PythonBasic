'''
Bài 03: Viết hàm
        def is_perfect(n)
    để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
    Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi
'''
print()
print("Bài 03: Viết hàm def is_perfect(n) để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, \ntrả lại True nếu có, False nếu không. \nGhi chú: Xem định nghĩa về số hoàn hảo: \nttp://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi")
print()
n = int(input("Nhập số tự nhiên N: "))
def is_perfect(n):
    tong = 0
    for i in range (1,n):
        if n % i == 0:
            tong = tong + i
    if tong == n:
        return n,"là số hoàn hảo"
    else:
        return n,"không phải là số hoàn hảo"
print(is_perfect(n))