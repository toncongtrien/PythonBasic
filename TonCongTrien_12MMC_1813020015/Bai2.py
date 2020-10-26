'''
Viết hàm với tham số truyền vào là một tháng và trả về mùa tương ứng trong 
năm. Sử dụng hàm vừa cài đặt, nhập vào một tháng và in ra màn hình mùa trong năm.
Thí dụ: Người dùng nhập vào tháng 2, in ra màn hình là mùa Xuân.
'''

def mua(thang):
    if (1 <= thang <= 3):
        return("Mùa Xuân")
    elif (4 <= thang <= 6):
        return("Mùa Hạ")
    elif (7 <= thang <= 9):
        return("Mùa Thu")
    elif (10 <= thang <= 12):
        return("Mùa Đông")
    else:
        return("Không tồn tại, nhập lại từ 1 đến 12!")
if __name__ == "__main__":
    thang = int(input("Nhập tháng : "))
    print("Tháng",thang,"là",mua(thang))