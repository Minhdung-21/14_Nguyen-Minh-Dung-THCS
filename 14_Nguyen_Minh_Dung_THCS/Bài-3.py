chuoi = input("Nhập vào một chuỗi: ")
ket_qua = ""
ky_tu_truoc = ' '
dang_o_dau_chuoi = True

for ky_tu in chuoi:
    if ky_tu != ' ':
        ket_qua += ky_tu
        ky_tu_truoc = ky_tu
        dang_o_dau_chuoi = False
    else:
        if ky_tu_truoc != ' ' and not dang_o_dau_chuoi:
            ket_qua += ' '
            ky_tu_truoc = ' '
if ket_qua and ket_qua[-1] == ' ':
    ket_qua_moi = ""
    for i in range(len(ket_qua)-1):
        ket_qua_moi += ket_qua[i]
    ket_qua = ket_qua_moi

print("Chuỗi sau khi xóa khoảng trắng thừa:")
print(ket_qua)