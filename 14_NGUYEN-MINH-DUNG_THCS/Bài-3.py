from math import *
a = int(input("Nhập tử số: "))
b = int(input("Nhập mẫu số: "))

if gcd(a, b) == 1:
    print("Phân số đã tối giản")
else:
    print("Phân số chưa tối giản")
