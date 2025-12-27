def dem_tu_trong_file(duong_dan: str) -> int:
    with open(duong_dan, "r", encoding="utf-8") as f:
        noi_dung = f.read()
    return len(noi_dung.split())

if __name__ == "__main__":
    print("Tổng số từ trong tập tin:", dem_tu_trong_file("vanban.txt"))
