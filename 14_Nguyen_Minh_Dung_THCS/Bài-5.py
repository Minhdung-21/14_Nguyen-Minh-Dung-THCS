n = int(input("Nhập số lượng phần tử: "))
danh_sach = []
ket_qua = []

print("Nhập các phần tử:")
for i in range(n):
    phan_tu = input(f"Phần tử {i+1}: ")
    danh_sach.append(phan_tu)

for phan_tu in danh_sach:
    da_co = False
    for item in ket_qua:
        if item == phan_tu:
            da_co = True
            break
    
    if not da_co:
        ket_qua.append(phan_tu)

print("Danh sách sau khi loại bỏ trùng lặp:")
print(ket_qua)