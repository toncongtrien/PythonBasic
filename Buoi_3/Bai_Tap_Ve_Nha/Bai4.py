'''
Bài 04: Viết hàm
        def is_prime(n)
    để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
'''
print()
print("Bài 04: Viết hàm def is_prime(n) để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, \nnếu có thì trả lại True, nếu không thì trả lại False")
print()
n = int(input("Nhập N: "))
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return "Là số nguyên tố"
    return "Không phải là số nguyên tố"
print(n,is_prime(n))