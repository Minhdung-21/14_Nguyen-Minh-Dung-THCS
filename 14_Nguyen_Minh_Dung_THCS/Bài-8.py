n = int(input("Nhập số lượng phần tử: "))
danh_sach = []

print("Nhập các phần tử:")
for i in range(n):
    phan_tu = input(f"Phần tử {i+1}: ")
    danh_sach.append(phan_tu)
k = int(input("Nhập số vị trí dịch chuyển (k): "))
k = k % n  
ket_qua = []
for i in range(n):
    ket_qua.append("")
for i in range(n):
    vi_tri_moi = (i + k) % n
    ket_qua[vi_tri_moi] = danh_sach[i]

print("Danh sách ban đầu:", danh_sach)
print(f"Danh sách sau khi dịch phải {k} vị trí:")
print(ket_qua)