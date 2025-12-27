import os
import sys
from thu_vien_chung.xu_ly_so import kiem_tra_so_nguyen_to

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
thu_vien_path = os.path.join(project_root, "thu_vien_chung")
sys.path.append(thu_vien_path)

import xu_ly_so  # noqa: E402

if __name__ == "__main__":
    n = 29
    kq = xu_ly_so.kiem_tra_so_nguyen_to(n)
    print(f"{n} là số nguyên tố? ->", kq)
