# name = input("Nhập tên: ")

# print("Xin chào", name)

# age = int(input("Nhập tuổi: "))

# if age >= 18:
#     print("Bạn là người lớn")
# else:
#     print("Bạn chưa đủ 18 tuổi")

# age = int(input("Nhập tuổi: "))

# if age < 6:
#     print("Trẻ nhỏ")
# if 6 <= age <= 17:
#     print("Học sinh")
# if 18 <= age <= 22:
#     print("Sinh viên")
# if age > 22:
#     print("Người đi làm")

# age = int(input("Nhập tuổi: "))

# if age < 6:
#     print("Trẻ nhỏ")
# elif 6 <= age <= 17:
#     print("Học sinh")
# elif 18 <= age <= 22:
#     print("Sinh viên")
# else:
#     print("Người đi làm")

# a = int(input("Nhập điểm: "))

# if a < 50:
#     print("F")
# elif 50 <= a <= 74:
#     print("C")
# elif 75 <= a <= 89:
#     print("B")
# elif 90 <= a <= 100:
#     print("A")


# a = int(input("Nhập điểm: "))

# if a < 0 or a > 100:
#     print("Điểm không hợp lệ")
# elif a < 50:
#     print("F")
# elif a <= 74:
#     print("C")
# elif a <= 89:
#     print("B")
# else:
#     print("A")

# diem = int(input("Nhập điểm: "))

# if diem < 0 or diem > 100:
#     print("Điểm không hợp lệ")
# elif diem >= 90:
#     print("Xuất sắc")
# elif diem >= 75:
#     print("Khá")
# elif diem >= 50:
#     print("Trung bình")
# else:
#     print("Yếu")

# n = int(input("nhập một số nguyên: "))

# if n % 2 == 0:
#     print(n, "là số chẵn")
# else:
#     print(n, "là số lẻ")

# n = int(input("Nhập một số nguyên: "))
# print(n, "là số chẵn" if n % 2 == 0 else "là số lẻ")

# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# c = int(input("Nhập số c: "))

# if a >= b and a >= c:
#     print("Số lớn nhất là:", a)
# elif b >= a and b >= c:
#     print("Số lớn nhất là:", b)
# else:
#     print("Số lớn nhất là:", c)


# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# c = int(input("Nhập số c: "))

# if a >= b and a >= c:
#     print("Số lớn nhất là:", a)
# elif b >= c:
#     print("Số lớn nhất là:", b)
# else:
#     print("Số lớn nhất là:", c)

# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# c = int(input("Nhập số c: "))

# print("Số lớn nhất là:", max(a, b, c))


# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# c = int(input("Nhập số c: "))

# # tìm số lớn nhất
# if a >= b and a >= c:
#     max_num = a
# elif b >= a and b >= c:
#     max_num = b
# else:
#     max_num = c

# # tìm số nhỏ nhất
# if a <= b and a <= c:
#     min_num = a
# elif b <= a and b <= c:
#     min_num = b
# else:
#     min_num = c

# print("Số lớn nhất là:", max_num)
# print("Số nhỏ nhất là:", min_num)

# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# c = int(input("Nhập số c: "))

# print("Số lớn nhất là:", max(a, b, c))
# print("Số nhỏ nhất là:", min(a, b, c))

# numbers = list(map(int, input("Nhập các số, cách nhau bởi dấu cách: ").split()))

# print("Số lớn nhất là:", max(numbers))
# print("Số nhỏ nhất là:", min(numbers))

# Nhập nhiều số, cách nhau bởi dấu cách
# numbers = list(map(int, input("Nhập các số: ").split()))

# # Tìm số lớn nhất và nhỏ nhất
# largest = max(numbers)
# smallest = min(numbers)

# print("Số lớn nhất là:", largest)
# print("Số nhỏ nhất là:", smallest)

# text = "apple banana orange"
# result = text.split()
# print(result)   # ['apple', 'banana', 'orange']


# text = "apple banana,orange"
# result = text.split(",")
# print(result)   # ['apple', 'banana', 'orange']

# text = "a b c d e"
# result = text.split(" ", 2)
# print(result)   # ['a', 'b', 'c d e']


# year = int(input("Nhập năm: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(year, "là năm nhuận")
# else:
#     print(year, "không phải là năm nhuận")


# years = list(map(int, input("Nhập các năm (cách nhau bởi dấu cách): ").split()))

# for year in years:
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         print(year, "là năm nhuận")
#     else:
#         print(year, "không phải là năm nhuận")

# a = float(input("Nhập số thứ nhất: "))
# b = float(input("Nhập số thứ hai: "))
# op = input("Nhập toán tử (+, -, *, /): ")

# if op == "+":
#     print("Kết quả:", a + b)
# elif op == "-":
#     print("Kết quả:", a - b)
# elif op == "*":
#     print("Kết quả:", a * b)
# elif op == "/":
#     if b != 0:
#         print("Kết quả:", a / b)
#     else:
#         print("Lỗi: không thể chia cho 0")
# else:
#     print("Toán tử không hợp lệ")


while True:
    a = input("Nhập số thứ nhất (hoặc 'exit' để thoát): ")
    if a.lower() == "exit":
        print("Thoát chương trình.")
        break

    a = float(a)
    b = float(input("Nhập số thứ hai: "))
    op = input("Nhập toán tử (+, -, *, /): ")

    if op == "+":
        print("Kết quả:", a + b)
    elif op == "-":
        print("Kết quả:", a - b)
    elif op == "*":
        print("Kết quả:", a * b)
    elif op == "/":
        if b != 0:
            print("Kết quả:", a / b)
        else:
            print("Lỗi: không thể chia cho 0")
    else:
        print("Toán tử không hợp lệ")
    
    print("-" * 30)  # in thêm dòng ngăn cách

