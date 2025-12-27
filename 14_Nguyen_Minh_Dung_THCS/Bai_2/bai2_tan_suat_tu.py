import re

def tach_tu(noi_dung: str):
    noi_dung = re.sub(r"[^0-9A-Za-zÀ-ỹà-ỹ\s]", " ", noi_dung)
    return noi_dung.lower().split()

def tan_suat_tu(duong_dan: str) -> dict:
    with open(duong_dan, "r", encoding="utf-8") as f:
        words = tach_tu(f.read())

    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

if __name__ == "__main__":
    freq = tan_suat_tu("vanban.txt")
    print("Danh sách từ và số lần xuất hiện:")
    for w, c in sorted(freq.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {w}: {c}")
