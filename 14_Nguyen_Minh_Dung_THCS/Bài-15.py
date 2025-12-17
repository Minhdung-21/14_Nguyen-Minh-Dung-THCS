n = int(input("Nhập số lượng phần tử của tuple: "))
danh_sach = []

print("Nhập các số nguyên:")
for i in range(n):
    so = int(input(f"Phần tử {i+1}: "))
    danh_sach.append(so)

tuple_goc = tuple(danh_sach)

tuple_chan = []
tuple_le = []

tong_chan = 0
tong_le = 0

for so in tuple_goc:
    if so % 2 == 0:
        tuple_chan.append(so)
        tong_chan += so
    else:
        tuple_le.append(so)
        tong_le += so

tuple_chan = tuple(tuple_chan)
tuple_le = tuple(tuple_le)

print(f"\nTuple gốc: {tuple_goc}")
print(f"Tuple số chẵn: {tuple_chan}")
print(f"Tổng số chẵn: {tong_chan}")
print(f"Tuple số lẻ: {tuple_le}")
print(f"Tổng số lẻ: {tong_le}")