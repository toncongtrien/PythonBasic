'''
Bài 02: Viết hàm
        def reverse_string(str)
    trả lại chuỗi đảo ngược của chuỗi str
'''
print()
print("Bài 02: Viết hàm trả lại chuỗi đảo ngược của chuỗi str")
print()
n = str(input("Nhập vào một chuỗi bất kì: "))
def reverse_string(n):
    return(str(n)[::-1])
print("Chuỗi đảo ngược của",n,"là",reverse_string(n))