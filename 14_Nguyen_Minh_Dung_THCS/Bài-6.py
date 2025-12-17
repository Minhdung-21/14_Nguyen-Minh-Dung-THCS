n = int(input("Nhập số lượng phần tử: "))
danh_sach = []

print("Nhập các số nguyên:")
for i in range(n):
    so = int(input(f"Phần tử {i+1}: "))
    danh_sach.append(so)

tong_chan = 0
tong_le = 0

for so in danh_sach:
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so

print("Danh sách:", danh_sach)
print("Tổng các số chẵn:", tong_chan)
print("Tổng các số lẻ:", tong_le)