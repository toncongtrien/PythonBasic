#Bài 10: Tính số fibo thứ n
print()
print("Bài 10: Tính số fibo thứ n")
n = int(input("Nhập N: "))
def fibonacci(n):
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("Số fibo thứ n là: ")
sb = ""
for i in range(n):
    sb = sb + str(fibonacci(i)) + ", "
print(sb)
