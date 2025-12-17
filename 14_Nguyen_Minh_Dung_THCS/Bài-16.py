chuoi = input("Nhập vào một chuỗi: ")

tan_suat = {}

for ky_tu in chuoi:
    da_co = False
    for key in tan_suat:
        if key == ky_tu:
            tan_suat[key] += 1
            da_co = True
            break

    if not da_co:
        tan_suat_moi = {}
        for key in tan_suat:
            tan_suat_moi[key] = tan_suat[key]
        tan_suat_moi[ky_tu] = 1
        tan_suat = tan_suat_moi

print("Tần suất xuất hiện của các ký tự:")
for ky_tu, so_lan in tan_suat.items():
    print(f"'{ky_tu}': {so_lan}")