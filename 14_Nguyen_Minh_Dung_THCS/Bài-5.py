
def kiem_tra_so_doi_xung(n):
    return str(n) == str(n)[::-1]

n = int(input("Nhập số để kiểm tra đối xứng: "))
print("Là số đối xứng?", kiem_tra_so_doi_xung(n))