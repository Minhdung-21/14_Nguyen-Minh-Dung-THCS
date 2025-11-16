n = int(input("Nhập số n : "))
S2 = 1  
for i in range(1, n):
    S2 *= i
print("Tích các số từ 1 đến", n, "là:", S2)