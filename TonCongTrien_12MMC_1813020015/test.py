#1
def manual_replace(s, list, index):
    return s[:index] + list + s[index +1:]
string = input("\t===> Nhập chuỗi: ")
print("\t===> Kết quả:\t",manual_replace(string, "$", 0))