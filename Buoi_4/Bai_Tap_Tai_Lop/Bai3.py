print("\n\tBài 03: Viết chương trình để xóa bỏ các ký tự \n\tcó chỉ số là số lẻ trong một chuỗi")
string = input("\t===> Nhập chuỗi: ")
def even_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 != 0:
      result = result + str[i]
  return "\t===> Kết quả: " + result
print(even_values_string(string))