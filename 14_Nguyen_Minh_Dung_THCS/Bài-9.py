n = int(input("Nhập kích thước ma trận vuông (n): "))
ma_tran = []
print("Nhập ma trận:")
for i in range(n):
    hang = []
    for j in range(n):
        gia_tri = int(input(f"Phần tử [{i}][{j}]: "))
        hang.append(gia_tri)
    ma_tran.append(hang)
tong = 0
for i in range(n):
    j = n - 1 - i 
    tong += ma_tran[i][j]

print("Ma trận:")
for hang in ma_tran:
    print(hang)

print("Tổng các phần tử trên đường chéo phụ:", tong)