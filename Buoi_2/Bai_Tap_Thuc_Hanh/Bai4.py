#Bai_4
print()
print("Tính tổng các số lẻ từ 0 đến N")
n = int(input("Nhập N = "))
le = 0
for i in range (0, n+1):
    if(i % 2 != 0):
        le += i
        print (i)
    else:
        print()
print()
print("Tổng các số lẻ là: ",le)