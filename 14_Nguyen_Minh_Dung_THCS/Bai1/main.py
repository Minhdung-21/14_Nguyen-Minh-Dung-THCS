from hinh_hoc import chu_vi_hinh_vuong, chu_vi_hinh_tron
if __name__ == "__main__":
    cv_vuong = chu_vi_hinh_vuong(5)
    cv_tron = chu_vi_hinh_tron(3)

    print("Chu vi hình vuông (cạnh=5):", cv_vuong)
    print("Chu vi hình tròn (bán kính=3):", cv_tron)
