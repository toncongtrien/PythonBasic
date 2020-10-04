'''
Bài 09: Viết hàm
        def change_upper_lower(str)
    chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
'''
print()
print("Bài 9: Chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str")
s = str(input("Nhập chuỗi: "))
print("Chuỗi vừa nhập là: ",s)
def count_upper_lower(s):
    print("Chuyển ký tự thường thành ký tự in hoa: ",s.upper())
    print("Chuyển ký tự in hoa thành ký tự thường: ",s.lower())
count_upper_lower(s)
