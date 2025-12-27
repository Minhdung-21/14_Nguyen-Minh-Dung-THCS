def lay_gia_tri(tu_dien: dict, khoa, mac_dinh=None):
    """Lấy giá trị theo khóa, có thể trả về mac_dinh nếu không tồn tại."""
    return tu_dien.get(khoa, mac_dinh)
