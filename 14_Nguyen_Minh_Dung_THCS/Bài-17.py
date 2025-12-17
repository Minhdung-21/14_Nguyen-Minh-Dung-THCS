n = int(input("Nhập số lượng cặp key-value: "))
dict_data = {}

print("Nhập các cặp key-value:")
for i in range(n):
    key = input(f"Key {i+1}: ")
    value = int(input(f"Value cho {key}: "))
    dict_data[key] = value

key_max = None
value_max = None

first = True
for key, value in dict_data.items():
    if first:
        key_max = key
        value_max = value
        first = False
    elif value > value_max:
        key_max = key
        value_max = value

print(f"\nDictionary: {dict_data}")
print(f"Key có giá trị lớn nhất: '{key_max}' với giá trị {value_max}")