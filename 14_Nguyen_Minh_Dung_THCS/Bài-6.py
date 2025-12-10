def la_so_nguyen_to(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    from math import sqrt
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to_trong_khoang(a, b):
    print(f"Số nguyên tố từ {a} đến {b}: ", end="")
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            print(i, end=" ")
    print()

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
in_so_nguyen_to_trong_khoang(a, b)