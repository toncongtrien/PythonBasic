#Bài 7: Xem 1 số có phải là số chính phương hay không
print()
print("Bài 7: Xem N số có phải là số chính phương hay không")
import math
n = int(input("Nhập N: "))
x = math.sqrt(n)
def sochingphuong(n):
    if(x * x == n):
        return n, "là số chính phương"
    else:
        return n, "không phải là số chính phương"
print(sochingphuong(n))