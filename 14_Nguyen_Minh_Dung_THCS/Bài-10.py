hang_so = int(input("Nhập số hàng: "))
cot_so = int(input("Nhập số cột: "))
ma_tran = []

print("Nhập ma trận:")
for i in range(hang_so):
    hang = []
    for j in range(cot_so):
        gia_tri = int(input(f"Phần tử [{i}][{j}]: "))
        hang.append(gia_tri)
    ma_tran.append(hang)

tong_lon_nhat = None
hang_tong_lon_nhat = 0

for i in range(hang_so):
    tong_hang = 0
    for j in range(cot_so):
        tong_hang += ma_tran[i][j]
    
    if tong_lon_nhat is None or tong_hang > tong_lon_nhat:
        tong_lon_nhat = tong_hang
        hang_tong_lon_nhat = i

print("Ma trận:")
for hang in ma_tran:
    print(hang)

print(f"Hàng có tổng lớn nhất là hàng {hang_tong_lon_nhat}")
print(f"Tổng hàng đó: {tong_lon_nhat}")