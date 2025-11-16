n = int(input("Nhập số n : "))
S4 = 0 
for k in range(0, n+1):     
    S4 += k / (k + 2)
print("Tổng S4 là:", S4)
