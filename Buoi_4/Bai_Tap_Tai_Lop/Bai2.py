print("\n\tBài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng,\n\tvới m là số không âm, nhập từ bàn phím.")
string = input("\t===> Nhập chuỗi: ")
def remove_char_m(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return "\t===> Kết quả: " + first_part + last_part
print(remove_char_m(string, int(input("\t===> Nhập thứ tự ký tự muốn xoá: "))))