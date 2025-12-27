def sao_chep(nguon: str, dich: str, chunk_size: int = 1024):
    with open(nguon, "rb") as f_src, open(dich, "wb") as f_dst:
        while True:
            data = f_src.read(chunk_size)
            if not data:
                break
            f_dst.write(data)

if __name__ == "__main__":
    src = "bai5_sao_chep_file.py"
    dst = "bai5_sao_chep_file_copy.py"
    sao_chep(src, dst)
    print(f"Đã sao chép {src} -> {dst}")
