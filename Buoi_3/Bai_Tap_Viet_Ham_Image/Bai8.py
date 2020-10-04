#Bài 8: Tính tổng các số nguyên tố từ 1 đến N
print()
print("Bài 8: Tính tổng các số nguyên tố từ 1 đến N")
n = int(input("Nhập N: "))
def songuyento(n):
    count = 0
    s = 0 
    for i in range(1, n + 1):
        if n % i == 0:
            s = s+i
            count += 1
    if count == 2:
        return s
    return n,"không phải là số nguyên tố"
print("Tổng các số nguyên tố là: ",songuyento(n))