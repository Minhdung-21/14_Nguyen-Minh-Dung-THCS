print("TẬP HỢP A")
n_a = int(input("Nhập số phần tử của tập A: "))
tap_a = []

print("Nhập các phần tử của tập A:")
for i in range(n_a):
    phan_tu = input(f"Phần tử {i+1}: ")
    tap_a.append(phan_tu)

print("\nTẬP HỢP B")
n_b = int(input("Nhập số phần tử của tập B: "))
tap_b = []

print("Nhập các phần tử của tập B:")
for i in range(n_b):
    phan_tu = input(f"Phần tử {i+1}: ")
    tap_b.append(phan_tu)

a_tru_b = []
for phan_tu in tap_a:
    co_trong_b = False
    for item in tap_b:
        if item == phan_tu:
            co_trong_b = True
            break
    if not co_trong_b:
        a_tru_b.append(phan_tu)

b_tru_a = []
for phan_tu in tap_b:
    co_trong_a = False
    for item in tap_a:
        if item == phan_tu:
            co_trong_a = True
            break
    if not co_trong_a:
        b_tru_a.append(phan_tu)

giao_ab = []
for phan_tu in tap_a:
    for item in tap_b:
        if item == phan_tu:
            da_co = False
            for g in giao_ab:
                if g == phan_tu:
                    da_co = True
                    break
            if not da_co:
                giao_ab.append(phan_tu)
            break
hop_ab = []
for phan_tu in tap_a:
    hop_ab.append(phan_tu)

for phan_tu in tap_b:
    da_co = False
    for item in hop_ab:
        if item == phan_tu:
            da_co = True
            break
    if not da_co:
        hop_ab.append(phan_tu)

print("\nKẾT QUẢ:")
print(f"A = {tap_a}")
print(f"B = {tap_b}")
print(f"A - B (thuộc A, không thuộc B): {a_tru_b}")
print(f"B - A (thuộc B, không thuộc A): {b_tru_a}")
print(f"A ∩ B (giao của A và B): {giao_ab}")
print(f"A ∪ B (hợp của A và B): {hop_ab}")