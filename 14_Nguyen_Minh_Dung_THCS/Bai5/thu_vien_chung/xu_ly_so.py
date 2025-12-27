def kiem_tra_so_nguyen_to(so: int) -> bool:
    """Trả về True nếu so là số nguyên tố, ngược lại False."""
    if not isinstance(so, int):
        return False
    if so < 2:
        return False
    if so == 2:
        return True
    if so % 2 == 0:
        return False
    i = 3
    while i * i <= so:
        if so % i == 0:
            return False
        i += 2
    return True
