'''
Bài 01: Viết hàm
def max_min(*numbers)
trả lại cả giá trị max, min của nhiều số được truyền vào
'''
print()
print("Bài 01: Viết hàm trả lại cả giá trị max, min của nhiều số được truyền vào")
print()
b = int(input('Nhập một số nguyên b bất kì: '))
a = [3,4,1,8,23,16,18,98,b]
max_ = 0
min_ = b
for i in a:
    if i < min_:
        min_ = i
for i in a:
    if i > max_:
        max_ = i
print("Max: ", max_)
print("Min: ", min_)