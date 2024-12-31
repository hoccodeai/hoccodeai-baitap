
def find_characters(str_input, find_characters):
    count = 0
    positions = []
    for i, char in enumerate(str_input):
        if char == find_characters:
            count += 1
            positions.append(i)
    print(f"Ký tự '{find_characters}' xuất hiện {count} lần")
    if count > 0:
        print(f"Vị trí xuất hiện của ký tự '{find_characters}': {positions}")

str_input = input("Nhập chuỗi: ")
find_characters = input("Nhập ký tự cần tìm: ")
find_characters(str_input, find_characters)
