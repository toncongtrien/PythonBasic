#Bài 1
print("\n\tBài 01: Viết chương trình thay thế tất cả các \n\tký tự giống ký tự đầu tiên của một Chuỗi thành $.")
def manual_replace(s, char, index):
    return s[:index] + char + s[index +1:]
string = input("\t===> Nhập chuỗi: ")
print("\t===> Kết quả:\t",manual_replace(string, "$", 0))

#Bài 2
print("\n\tBài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng,\n\tvới m là số không âm, nhập từ bàn phím.")
string = input("\t===> Nhập chuỗi: ")
def remove_char_m(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return "\t===> Kết quả: " + first_part + last_part
print(remove_char_m(string, int(input("\t===> Nhập thứ tự ký tự muốn xoá: "))))

#Bài 3
print("\n\tBài 03: Viết chương trình để xóa bỏ các ký tự \n\tcó chỉ số là số lẻ trong một chuỗi")
string = input("\t===> Nhập chuỗi: ")
def even_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 != 0:
      result = result + str[i]
  return "\t===> Kết quả: " + result
print(even_values_string(string))

#Bài 4
print("\n\tBài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối \n\ttrong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng. ")
string = input("\t===> Nhập chuỗi: ")
def string_both_ends(str):
  if len(str) < 2:
    return "\t===> Chuỗi rỗng"
  return "\t===> Kết quả: " + str[0:2] + str[-2:]
print(string_both_ends(string))

#Bài 5
print("\n\tBài 05: Viết chương trình tìm ra ký tự lớn nhất và \n\tký tự nhỏ nhất của một chuỗi nhập từ bàn phím.")
print("\tLưu ý: Chuỗi được sắp xếp theo thứ tự từ nhỏ đến lớn \n\ttrong bảng ký tự ASCII (A, B, C,..., x, y, z.)")
string = input("\t===> Nhập chuỗi: ")
print("\t===> Ký tự lớn nhất trong chuỗi là: ", max(string))
print("\t===> Ký tự nhỏ nhất trong chuỗi là: ", min(string))

#Bài 6
print("\n\tBài 06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa \n\tvà từ ký tự hoa sang ký tự thường trong một chuỗi.")
string = input("\t===> Nhập chuỗi: ")
print("\t===> Kết quả: " + string.swapcase())