print("\n\tBài 01: Viết chương trình thay thế tất cả các \n\tký tự giống ký tự đầu tiên của một Chuỗi thành $.")
def manual_replace(s, char, index):
    return s[:index] + char + s[index +1:]
string = input("\t===> Nhập chuỗi: ")
print("\t===> Kết quả:\t",manual_replace(string, "$", 0))