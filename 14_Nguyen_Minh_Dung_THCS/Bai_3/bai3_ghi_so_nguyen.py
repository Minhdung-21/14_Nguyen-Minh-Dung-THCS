if __name__ == "__main__":
    ds = [10, -3, 25, 0, 7, 99, 42]
    with open("so_nguyen.txt", "w", encoding="utf-8") as f:
        for so in ds:
            f.write(str(so) + "\n")
    print("Đã tạo file so_nguyen.txt")
