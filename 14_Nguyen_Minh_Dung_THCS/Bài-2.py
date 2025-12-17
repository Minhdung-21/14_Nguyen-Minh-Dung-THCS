s = input("Nhập chuỗi: ")
n = int(input("Nhập độ dài n: "))
s = s + " " 
tu_hien_tai = ""
danh_sach_kq = []
for ky_tu in s:
    if ky_tu != " ":
        tu_hien_tai = tu_hien_tai + ky_tu
    else:
        dem_ky_tu = 0
        for _ in tu_hien_tai: 
            dem_ky_tu += 1
        if dem_ky_tu > n:
            danh_sach_kq = danh_sach_kq + [tu_hien_tai]
        tu_hien_tai = ""

print("Các từ có độ dài lớn hơn", n, "là:", danh_sach_kq)