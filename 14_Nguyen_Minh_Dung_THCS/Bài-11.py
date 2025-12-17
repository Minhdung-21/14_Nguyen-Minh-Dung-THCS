n = int(input("Nhập kích thước ma trận vuông (n): "))
ma_tran = []

print("Nhập ma trận:")
for i in range(n):
    hang = []
    for j in range(n):
        gia_tri = int(input(f"Phần tử [{i}][{j}]: "))
        hang.append(gia_tri)
    ma_tran.append(hang)

la_doi_xung = True

for i in range(n):
    for j in range(i+1, n):
        if ma_tran[i][j] != ma_tran[j][i]:
            la_doi_xung = False
            break
    if not la_doi_xung:
        break

print("Ma trận:")
for hang in ma_tran:
    print(hang)

if la_doi_xung:
    print("Ma trận này là ma trận đối xứng")
else:
    print("Ma trận này KHÔNG phải ma trận đối xứng")