'''
Bài 05: Viết hàm
        def count_upper_lower(str)
    trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
'''
print()
print("Bài 05: Viết hàm \ndef count_upper_lower(str) \ntrả lại số lượng chữ cái viết hoa, \nsố lượng chữ cái viết thường trong chuỗi str")
print()
s = str(input("Viết một câu: "))
def count_upper_lower(s):
    count_upper = 0
    count_lower = 0
    for c in s:
        if c.isupper():
            count_upper += 1
        if c.islower():
            count_lower += 1
    print("Câu đã nhập là: ",s)
    print("Số chữ in hoa: ", count_upper)
    print("Số chữ thường: ", count_lower)
count_upper_lower(s)