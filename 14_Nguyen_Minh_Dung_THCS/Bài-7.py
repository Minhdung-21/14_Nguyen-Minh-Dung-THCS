n = int(input("Nhập số lượng phần tử: "))
danh_sach = []

print("Nhập các số nguyên:")
for i in range(n):
    so = int(input(f"Phần tử {i+1}: "))
    danh_sach.append(so)

target = int(input("Nhập giá trị tổng cần tìm: "))

cac_cap = []

for i in range(len(danh_sach)):
    for j in range(i+1, len(danh_sach)):
        if danh_sach[i] + danh_sach[j] == target:
            cac_cap.append((danh_sach[i], danh_sach[j]))

print("Danh sách:", danh_sach)
print(f"Các cặp số có tổng bằng {target}:")
if cac_cap:
    for cap in cac_cap:
        print(f"{cap[0]} + {cap[1]}")
else:
    print("Không tìm thấy cặp nào")