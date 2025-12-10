def tinh_tong_chu_so(n):
    if n == 0:
        return 0
    return n % 10 + tinh_tong_chu_so(n // 10)

n = int(input("Nhập số để tính tổng chữ số (đệ quy): "))
print("Tổng chữ số =", tinh_tong_chu_so(n))