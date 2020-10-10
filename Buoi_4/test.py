def a(text):
    chars = "\\`*_{}[]()>#+-.!$"
    for c in chars:
        text = text.replace(c, "\\" + c)

s = "abc&def#ghi"
print(s.translate(str.maketrans({'&': '\&', '#': '\#'})))