n = int(input("Nhập số lượng cặp key-value: "))
dict_goc = {}

print("Nhập các cặp key-value (value là số):")
for i in range(n):
    key = input(f"Key {i+1}: ")
    value = int(input(f"Value cho {key}: "))
    dict_goc[key] = value
print("\nChọn điều kiện lọc:")
print("1. Giá trị lớn hơn một số")
print("2. Giá trị nhỏ hơn một số")
print("3. Giá trị bằng một số")
print("4. Giá trị trong khoảng")
chon = int(input("Lựa chọn của bạn: "))

dict_loc = {}

if chon == 1:
    nguong = int(input("Nhập ngưỡng (lớn hơn): "))
    for key, value in dict_goc.items():
        if value > nguong:
            dict_loc[key] = value
    dieu_kien = f"lớn hơn {nguong}"
    
elif chon == 2:
    nguong = int(input("Nhập ngưỡng (nhỏ hơn): "))
    for key, value in dict_goc.items():
        if value < nguong:
            dict_loc[key] = value
    dieu_kien = f"nhỏ hơn {nguong}"
    
elif chon == 3:
    nguong = int(input("Nhập giá trị (bằng): "))
    for key, value in dict_goc.items():
        if value == nguong:
            dict_loc[key] = value
    dieu_kien = f"bằng {nguong}"
    
elif chon == 4:
    tu = int(input("Nhập giá trị từ: "))
    den = int(input("Nhập giá trị đến: "))
    for key, value in dict_goc.items():
        if value >= tu and value <= den:
            dict_loc[key] = value
    dieu_kien = f"từ {tu} đến {den}"

print(f"\nDictionary gốc: {dict_goc}")
print(f"\nDictionary sau khi lọc (giá trị {dieu_kien}):")
if dict_loc:
    print(dict_loc)
else:
    print("Không có phần tử nào thỏa mãn điều kiện")