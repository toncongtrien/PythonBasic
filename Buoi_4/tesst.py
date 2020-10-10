'''
-	Viết 1 hàm sayHello(name): gọi lại hàm và truyền vào 1 giá tri tên của mình in kết quả ra màn hình. 
Ví dụ nhập tên là  Minh Tân thì xuất ra là “Xin chào bạn Minh Tân”
'''
# def say_hello(name):
#     hello_string = "Xin chào "+name+ " "
#     print("=" * (len(hello_string)))
#     print("|" + hello_string + " |")
#     print("=" * (len(hello_string)+2))

# a_name = input("Tên của bạn là gì: ")
# say_hello(a_name)

'''
Viết hàm với tham số truyền vào là năm sinh, 
sử dụng hàm vừa cài đặt, nhập vào năm sinh và in ra tuổi:
'''
# def tinh_tuoi(year):
#     kq = 2020 - year
#     return kq

# from datetime import date,datetime
# def tinh_tuoi(year):
#     # nam_hien_tai = date.today()
#     return date.today().year - year

# a_year = int(input("Nhập vào số năm sinh: "))
# # kq = tinh_tuoi(a_year)
# print(f"Tuổi của bạn là: {tinh_tuoi(a_year)}")

'''
Viết hàm với tham số truyền vào là nhiệt độ F, 
trả về kết quả nhiệt độ C theo công thức. 
Sử dụng hàm vừa cài đặt, nhập vào độ F và in ra màn hình độ C.
C = 5*(F - 32) / 9, với C: nhiệt độ C; F: nhiệt độ F

'''
# def tinh_do(f):
#     return round(5*(f - 32) / 9,2)

# tinh_do_lambda = lambda f : round(5*(f - 32) / 9,2)

# f = int(input("Nhập vào f: "))
# # kq = tinh_do(f)
# kq = tinh_do_lambda(f)
# print(f"Độ c: {kq}")

'''
Viết hàm với tham số truyền vào là một tháng và trả về mùa tương ứng trong năm. 
Sử dụng hàm vừa cài đặt, nhập vào một tháng và in ra màn hình mùa trong năm.
Thí dụ: Người dùng nhập vào tháng 2, in ra màn hình là mùa Xuân.
Từ tháng 1 đến tháng 3: Mùa Xuân, Từ tháng 4 đến tháng 6: Mùa Hạ,
Từ tháng 7 đến tháng 9: Mùa Thu,Từ tháng 10 đến tháng 12: Mùa Đông
'''
# def nhap_dl():
#     while True:
#         n = input("Nhập vào tháng: ")
#         if n.isnumeric():
#             n = int(n)
#             if 1 <= n <= 12:
#                 print(f"Bạn đã nhập tháng: {n}")
#                 return n
#             print("Nhập sai! Nhập lại")
#         print("Xin vui lòng nhập lại theo đúng định dạng (1 -> 12)")

# def cac_mua(thang):
#     if 1 <= thang <= 3:
#         return 1
#     elif 4 <= thang <= 6:
#         return 2
#     elif 7 <= thang <= 9:
#         return 3
#     else:
#         return 4

# a_thang = nhap_dl()
# kq = cac_mua(a_thang)
# if kq == 1:
#     print("Mùa xuân")
# elif kq == 2:
#     print("Mùa hạ")
# elif kq == 3:
#     print("Mùa Thu")
# else:
#     print("Mùa đông")


# a_test = input("Nhập vào cái gì đó: ")
# print(f"Giá trị bạn vừa nhập là: {a_test}")
# print(type(a_test))

'''
Viết hàm tìm số lớn nhất và nhỏ nhất của hai số nguyên a và b; sử dụng hàm vừa cài đặt, 
nhập vào 3 số nguyên a, b, c và tìm số lớn nhất và nhỏ nhất trong 3 số đó.
'''

# def max_min(*numbers):
#     max = min = numbers[0]
#     for number in numbers:
#         if min > number:
#             min = number
#         if max < number:
#             max = number
#     return max,min

# a_max,a_min = max_min(454,45,87,34,68,35,65,78)
# print(f"Giá trị lớn nhất là: {a_max}")
# print(f"Giá trị nhỏ nhất là: {a_min}")

