#Bài 6: Xem 1 số có phải là số nguyên tố hay không
print()
print("Bài 6: Xem N số có phải là số nguyên tố hay không")
n = int(input("Nhập N: "))
def songuyento(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return n, "là số nguyên tố"
    return n, "không phải là số nguyên tố"
print(songuyento(n))