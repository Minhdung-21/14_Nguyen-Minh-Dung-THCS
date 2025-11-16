from math import *
n = int(input("Nhập số n : "))
print("Các số nguyên tố nhỏ hơn n:")
for i in range(2, n):         
    a = True             
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            a = False 
            break               
    if a:
        print(i, end=" ")  