n = int(input("Nhập số lượng phần tử: "))
danh_sach = []
print("Nhập các số nguyên:")
for i in range(n):
    so = int(input(f"Phần tử {i+1}: "))
    danh_sach.append(so)
lon_nhat = danh_sach[0]
for so in danh_sach:
    if so > lon_nhat:
        lon_nhat = so
lon_thu_hai = danh_sach[0]
if lon_thu_hai == lon_nhat:
    lon_thu_hai = danh_sach[1] if len(danh_sach) > 1 else danh_sach[0]

for so in danh_sach:
    if so > lon_thu_hai and so != lon_nhat:
        lon_thu_hai = so

print("Danh sách:", danh_sach)
print("Giá trị lớn thứ hai là:", lon_thu_hai)