import csv

if __name__ == "__main__":
    file_path = "nhan_vien.csv"
    rows = [
        {"ID": "1", "Tên": "An", "Lương": "45000"},
        {"ID": "2", "Tên": "Bình", "Lương": "52000"},
        {"ID": "3", "Tên": "Chi", "Lương": "75000"},
        {"ID": "4", "Tên": "Dũng", "Lương": "50000"},
        {"ID": "5", "Tên": "Hà", "Lương": "91000"},
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "Tên", "Lương"])
        writer.writeheader()
        writer.writerows(rows)

    with open(file_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print("Nhân viên có lương > 50000:")
        for row in reader:
            luong = int(row["Lương"])
            if luong > 50000:
                print(f"- ID: {row['ID']} | Tên: {row['Tên']} | Lương: {luong}")
