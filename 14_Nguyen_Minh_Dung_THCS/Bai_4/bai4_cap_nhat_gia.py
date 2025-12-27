def cap_nhat_gia(file_path: str, id_sp: str, gia_moi: str) -> bool:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip()]

    if not lines:
        return False

    header = lines[0]
    updated_lines = [header]
    updated = False

    for line in lines[1:]:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 3:
            updated_lines.append(line)
            continue

        pid, ten, gia = parts[0], parts[1], parts[2]
        if pid == id_sp:
            gia = gia_moi
            updated = True
        updated_lines.append(f"{pid}, {ten}, {gia}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(updated_lines) + "\n")

    return updated

if __name__ == "__main__":
    file_path = "san_pham.txt"
    id_sp = input("Nhập ID sản phẩm cần cập nhật giá: ").strip()
    gia_moi = input("Nhập giá mới: ").strip()

    ok = cap_nhat_gia(file_path, id_sp, gia_moi)
    print("Cập nhật thành công." if ok else "Không tìm thấy ID cần cập nhật.")
