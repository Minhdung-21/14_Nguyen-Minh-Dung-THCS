n = int(input("Nhập kích thước ma trận (n): "))
ma_tran = []

print("Nhập ma trận:")
for i in range(n):
    hang = []
    for j in range(n):
        gia_tri = int(input(f"Phần tử [{i}][{j}]: "))
        hang.append(gia_tri)
    ma_tran.append(hang)

la_don_vi = True
for i in range(n):
    for j in range(n):
        if i == j:
            if ma_tran[i][j] != 1:
                la_don_vi = False
                break
        else:
            if ma_tran[i][j] != 0:
                la_don_vi = False
                break
    if not la_don_vi:
        break

print("Ma trận:")
for hang in ma_tran:
    print(hang)

if la_don_vi:
    print("Đây là ma trận đơn vị")
else:
    print("Đây KHÔNG phải ma trận đơn vị")