n = int(input("Nhập số lượng cặp key-value: "))
dict_goc = {}

print("Nhập các cặp key-value (đảm bảo các value là duy nhất):")
values = []

for i in range(n):
    key = input(f"Key {i+1}: ")
    
    while True:
        value = input(f"Value cho {key}: ")
        
        da_co = False
        for v in values:
            if v == value:
                da_co = True
                break
        
        if da_co:
            print("Value này đã tồn tại! Vui lòng nhập value khác.")
        else:
            values.append(value)
            dict_goc[key] = value
            break

dict_dao_nguoc = {}

for key, value in dict_goc.items():
    dict_dao_nguoc[value] = key

print(f"\nDictionary gốc: {dict_goc}")
print(f"Dictionary đảo ngược: {dict_dao_nguoc}")