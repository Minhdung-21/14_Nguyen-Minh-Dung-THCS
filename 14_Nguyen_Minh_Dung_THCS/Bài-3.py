def kiem_tra_so_armstrong(n):
    tong = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        tong += digit ** 3
        temp //= 10
    return tong == n

n = int(input("Nhập số để kiểm tra Armstrong: "))
print("Là số Armstrong?" , kiem_tra_so_armstrong(n))