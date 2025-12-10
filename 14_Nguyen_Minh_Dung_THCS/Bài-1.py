def chuyen_doi_nhiet_do(do_c):
    return do_c * 9/5 + 32

do_c = float(input("Nhập độ C: "))
print("Độ F là:", chuyen_doi_nhiet_do(do_c))