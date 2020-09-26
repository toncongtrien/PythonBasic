#Bai4
from math import sqrt
print()
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if( (a<b+c)&(b<a+c)&(c<a+b) ):
    if( (a*a==b*b+c*c) | (b*b==a*a+c*c) | (c*c== a*a+b*b)):
       print("==> Tam giác vuông")
    else:
       print("==> Tam giác, nhưng không phải là hình tam giác vuông")
else:
    print("==> Không phải hình tam giác")