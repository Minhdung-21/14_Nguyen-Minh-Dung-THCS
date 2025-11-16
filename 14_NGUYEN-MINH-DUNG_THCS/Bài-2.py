a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
ucln = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        ucln = i
print(f"Ước chung lớn nhất của {a} và {b} là: {ucln}")
