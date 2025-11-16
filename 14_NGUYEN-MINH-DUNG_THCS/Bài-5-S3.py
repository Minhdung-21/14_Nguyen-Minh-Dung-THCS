n = int(input("Nhập số n : "))
S3 = 0
for i in range(1, n+1):
    S3 += (-1)**(i+1) * 1/i
print("Tổng S3 là:", S3)