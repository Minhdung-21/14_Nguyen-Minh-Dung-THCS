def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

def tinh_tong_so_hoan_hao(a, b):
    tong = 0
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            tong += i
    return tong

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Tổng số hoàn hảo trong khoảng là:", tinh_tong_so_hoan_hao(a, b))