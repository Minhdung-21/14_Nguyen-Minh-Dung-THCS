import math

def luy_thua(co_so: float, so_mu: float) -> float:
    return co_so ** so_mu

def can_bac_hai(so: float) -> float:
    if so < 0:
        raise ValueError("Không thể tính căn bậc hai của số âm.")
    return math.sqrt(so)
