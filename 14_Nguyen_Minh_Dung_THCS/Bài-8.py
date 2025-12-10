def tim_so_le_lon_nhat(a, b, c):
    le = [x for x in (a, b, c) if x % 2 != 0]
    return max(le) if le else -1

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
print("Số lẻ lớn nhất là:", tim_so_le_lon_nhat(a, b, c))