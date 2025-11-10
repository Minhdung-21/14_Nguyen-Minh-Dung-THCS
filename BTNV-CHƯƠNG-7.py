# BÀI 1
a = (int(input("Giá sản phẩm : ")))
b = (int(input("Số lượng sản phẩm : ")))
Tong_chi_phi = (a * b * 0.10 )+ (a * b)
print("Tổng chi phí là : ", "%.2f " % Tong_chi_phi)

# BÀI 2
a = (int(input("Tổng số kẹo : ")))
b = (int(input("Số học sinh : ")))
so_keo_moi_hoc_sinh = a // b
so_keo_con_lai = a % b
print("Mỗi học sinh được : ", so_keo_moi_hoc_sinh)
print("Số kẹo còn lại : ", so_keo_con_lai)

# BÀI 3
a = (int(input("Nhập độ dài cạnh đáy : ")))
b = (int(input("Nhập chiều cao của tam giác : ")))
dien_tich_tam_giac = (a * b) / 2
print("Diện tích tam giác là : ", dien_tich_tam_giac)

# BÀI 4
a = (int(input("Nhập số tiền VND : ")))
tien_USD = a / 24.500
print("Số tiền USD là : ", "%.2f " % tien_USD)

# BÀI 5
# Nhập dữ liệu
a = float(input("Số tiền gửi ban đầu (VNĐ): "))
b = float(input("Lãi suất năm (%/năm): ")) / 100 

# Tính lãi (lãi đơn)
so_tien_lai_sau_1_thang = a * b * (1/12)
so_tien_lai_sau_2_quy = a * b * (6/12)
so_tien_lai_sau_3_nam = a * b * 3

# In kết quả
print("Số tiền lãi sau 1 tháng là:", round(so_tien_lai_sau_1_thang, 2), "VNĐ")
print("Số tiền lãi sau 2 quý là:", round(so_tien_lai_sau_2_quy, 2), "VNĐ")
print("Số tiền lãi sau 3 năm là:", round(so_tien_lai_sau_3_nam, 2), "VNĐ")


# BÀI 6
a = (int(input("Nhập năm : ")))
nam_nhuan = (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)
print("Năm nhuận : ", nam_nhuan)

# BÀI 7
a = (input("Tên đăng nhập : "))
b = (input("Mật khẩu : "))
ten_dang_nhap = "admin"
mat_khau = "password123"
print("Kết quả : ", a == ten_dang_nhap and b == mat_khau)

# BÀI 8
a = (float(input("Cân nặng của bạn : ")))
b = (float(input("Chiều cao của bạn (m) : ")))
BMI = a / (b * b)
print("Chỉ số BMI của bạn là : ", "%.2f " % BMI)

# BÀI 9
a = (float(input("Số kWh đã tiêu thụ : ")))
bac_1 = a > 0 and a <= 100
bac_2 = a > 101 and a <= 200
bac_3 = a > 201 and a <= 300
gia_bac_1 = a * 1.678 
gia_bac_2 = a* 1.734
gia_bac_3 = a * 2.014
tong_tien = (bac_1 * gia_bac_1) + (bac_2 * gia_bac_2) + (bac_3 * gia_bac_3)
print("Tổng tiền điện phải trả là : ", tong_tien)

# BÀI 10
a = (float(input("Mức lương cơ bản : ")))
b = (int(input("Số ngày công trong tháng : ")))
luong_1_ngay = a / 22
tang_luong = b > 22
phat = b < 22
luong_thang = luong_1_ngay * b
tong_luong = luong_thang + (luong_thang * 0.10 * tang_luong) - (luong_thang * 0.05 * phat)
print("Tổng lương tháng là : ", tong_luong)