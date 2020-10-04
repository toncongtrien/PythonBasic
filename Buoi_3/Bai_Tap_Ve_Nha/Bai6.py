'''
Bài 06: Viết hàm
        def is_pangram(str, alphabet)
    đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
    Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần
'''
import string
print()
print("Bài 06: Viết hàm def is_pangram(str, alphabet) đề kiểm tra xem chuỗi str có phải là Pangram không, \ntrả lại True nếu có, False nếu không. \nGhi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần")
print()
gram = str(input("Nhập một chuỗi bất kì: "))
def is_pangram (gram):
       gram = gram.lower()
       gram_list_old = sorted([c for c in gram if c != ' '])
       gram_list = []
       for c in gram_list_old:
           if c not in gram_list:
               gram_list.append(c)
       if gram_list == list(string.ascii_lowercase): return True
       else: return False
print(is_pangram(gram))