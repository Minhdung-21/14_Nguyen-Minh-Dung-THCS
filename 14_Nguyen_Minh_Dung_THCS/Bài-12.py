print("MA TRẬN A:")
hang_a = int(input("Số hàng của ma trận A: "))
cot_a = int(input("Số cột của ma trận A: "))
ma_tran_a = []

print("Nhập ma trận A:")
for i in range(hang_a):
    hang = []
    for j in range(cot_a):
        gia_tri = int(input(f"A[{i}][{j}]: "))
        hang.append(gia_tri)
    ma_tran_a.append(hang)

print("\nMA TRẬN B:")
hang_b = int(input("Số hàng của ma trận B: "))
cot_b = int(input("Số cột của ma trận B: "))
ma_tran_b = []

print("Nhập ma trận B:")
for i in range(hang_b):
    hang = []
    for j in range(cot_b):
        gia_tri = int(input(f"B[{i}][{j}]: "))
        hang.append(gia_tri)
    ma_tran_b.append(hang)

if cot_a != hang_b:
    print("Không thể nhân hai ma trận này!")
    print(f"Số cột của A ({cot_a}) phải bằng số hàng của B ({hang_b})")
else:
    ket_qua = []
    for i in range(hang_a):
        hang = []
        for j in range(cot_b):
            hang.append(0)
        ket_qua.append(hang)
    
    for i in range(hang_a):
        for j in range(cot_b):
            tong = 0
            for k in range(cot_a):
                tong += ma_tran_a[i][k] * ma_tran_b[k][j]
            ket_qua[i][j] = tong
    
    print("\nMa trận A:")
    for hang in ma_tran_a:
        print(hang)
    
    print("\nMa trận B:")
    for hang in ma_tran_b:
        print(hang)
    
    print("\nKết quả A x B:")
    for hang in ket_qua:
        print(hang)