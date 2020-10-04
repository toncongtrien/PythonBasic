#Bài 9: In ra bảng cửu chương n 
print()
print("Bài 9: In ra bảng cửu chương n ")
n = int(input("Nhập N: "))
def bangcuuchuong(n):
    for j in range(1,11):
        s = n * j
        print(n, "*" ,j, "=" ,s)
    return 
print(bangcuuchuong(n))