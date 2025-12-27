from du_lieu.danh_sach import sap_xep_tang_dan
from du_lieu.tu_dien import lay_gia_tri

if __name__ == "__main__":
    ds = [9, 2, 7, 1, 5, 3]
    print("Danh sách ban đầu:", ds)
    print("Sắp xếp tăng dần:", sap_xep_tang_dan(ds))

    td = {"ten": "Dung", "truong": "UNETI", "nam": 2025}
    print("Lấy 'truong':", lay_gia_tri(td, "truong"))
    print("Lấy 'lop' (không có):", lay_gia_tri(td, "lop", mac_dinh="Chưa có"))
