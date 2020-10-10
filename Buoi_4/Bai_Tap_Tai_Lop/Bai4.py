print("\n\tBài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối \n\ttrong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng. ")
string = input("\t===> Nhập chuỗi: ")
def string_both_ends(str):
  if len(str) < 2:
    return "\t===> Chuỗi rỗng"
  return "\t===> Kết quả: " + str[0:2] + str[-2:]
print(string_both_ends(string))