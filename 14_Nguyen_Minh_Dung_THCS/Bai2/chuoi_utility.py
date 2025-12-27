def dao_nguoc_chuoi(chuoi: str) -> str:
    """Đảo ngược chuỗi."""
    return chuoi[::-1]
def dem_so_tu(chuoi: str) -> int:
    """Đếm số từ (tách theo khoảng trắng)."""
    words = chuoi.strip().split()
    return len(words)
