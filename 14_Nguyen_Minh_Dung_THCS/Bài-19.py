n = int(input("Nhập số lượng sinh viên: "))
sinh_vien = {}

print("Nhập thông tin sinh viên (tên: điểm):")
for i in range(n):
    ten = input(f"Tên sinh viên {i+1}: ")
    diem = int(input(f"Điểm của {ten}: "))
    sinh_vien[ten] = diem

nhom_diem = {}

for ten, diem in sinh_vien.items():
    da_co = False
    for key in nhom_diem:
        if key == diem:
            nhom_diem[diem].append(ten)
            da_co = True
            break
    if not da_co:
        nhom_diem[diem] = [ten]

print(f"\nDictionary gốc: {sinh_vien}")
print(f"\nDictionary nhóm theo điểm số: {nhom_diem}")