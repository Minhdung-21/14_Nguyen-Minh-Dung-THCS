import os

if __name__ == "__main__":
    temp_dir = "temp_files"
    os.makedirs(temp_dir, exist_ok=True)

    src_file = os.path.join(temp_dir, "file.txt")
    with open(src_file, "w", encoding="utf-8") as f:
        f.write("Đây là file tạm.\n")

    renamed_file = os.path.join(temp_dir, "new_file.txt")
    os.rename(src_file, renamed_file)
    moved_file = os.path.join(os.getcwd(), "new_file.txt")
    if os.path.exists(moved_file):
        moved_file = os.path.join(os.getcwd(), "new_file_moved.txt")

    os.rename(renamed_file, moved_file)
    os.rmdir(temp_dir)

    print("Đã tạo/đổi tên/di chuyển file và xóa thư mục temp_files.")
    print("File hiện tại nằm ở:", moved_file)
