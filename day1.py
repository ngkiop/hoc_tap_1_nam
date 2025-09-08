"""
print("Hello world !!!")

# Đây là comment 1 dòng
print("Xin chào")
"""

"""
Đây là comment nhiều dòng
"""

"""
print("Python rất dễ học")
"""

"""# In tên
print("Tên tôi là Ngk")

# In tuổi
print("Tôi 26 tuổi")
"""

"""
# Tạo biến thông tin cá nhân
name = "Ngk"
age = 26
height = 1.76

# In ra biến và kiểu dữ liệu của nó
print(name, type(name))
print(age, type(age))
print(height, type(height))

# Thử toán tử số học
x = 12
y = 3

print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x // y =", x // y)
print("x % y =", x % y)
print("x ** y =", x ** y)
"""

"""
name = input("Nhập tên của bạn: ")
print("Xin chào", name)
"""

"""
age = input("Nhập tuổi của bạn: ")
print(type(age)) # Luôn là str

age = int(age) # Ép kiểu về int
print(type(age)) # Kiểu int
print("Năm sau bạn sẽ", age + 1, "tuổi")
"""

"""
name = input("Nhập tên của bạn: ")
age = int(input("Nhập tuổi của bạn: "))

print("Xin chào", name, "bạn năm nay", age, "tuổi")
"""

"""
age = int(input("Nhập tuổi: "))

if age < 18:
    print("Bạn còn là trẻ em")
elif age < 30:
    print("Bạn là thanh niên")
else:
    print("Bạn là người lớn")
"""

"""
x = 10
print(x > 5 and x < 20) # True
print(x > 5 or x < 20)  # True
print(not(x == 10)) # False 
"""

"""
# Cách 1 cơ bản
so = int(input("Nhập số: "))

if so % 2 == 0:
    print("Đây là số chẵn")
else:
    print("Đây là số lẻ")
"""

"""
# Cách 2 dùng toán tử 3 ngôi
so = int(input("Nhập số: "))
print("Đây là số chẵn" if so % 2 == 0 else "Đây là số lẻ")
"""

"""
# Cách 3 dùng dictionary
so = int(input("Nhập số: "))
ketqua = {0: "Đây là số chẵn", 1: "Đây là số lẻ"}
print(ketqua[so % 2])
"""

"""
# Cách 4 dùng hàm
def kiem_tra_chan_le(n):
    if n % 2 == 0:
        return "Đây là số chẵn"
    else:
        return "Đây là số lẻ"
    
so = int(input("Nhập số: "))
print(kiem_tra_chan_le(so))
"""

"""
# Cách 5 dùng toán tử AND, OR và bitwise
num = int(input("Nhập số: "))
if num & 1 == 0:
    print("Đây là số chẵn")
else:
    print("Đây là số lẻ")
"""

"""
# Cách 6 dùng vòng lặp for
num = int(input("Nhập số: "))
for i in [num % 2]:
    if i == 0:
        print("Đây là số chẵn")
    else:
        print("Đây là số lẻ")
"""

"""
# Cách 7 dùng match-case (Python 3.10+)
num = int(input("Nhập số: "))
match num % 2:
    case 0:
        print("Đây là số chẵn")
    case 1:
        print("Đây là số lẻ")
"""

"""
# Cách 8 dùng tuple
num = int(input("Nhập số: "))
print(("Đây là số chẵn", "Đây là số lẻ")[num % 2])
"""

"""
# Cách 9 dùng lambda
num = int(input("Nhập số: "))
check = lambda x: {0: "Đây là số chẵn", 1: "Đây là số lẻ"}[x % 2]
print(check(num))
"""

"""
# Cách 10 dùng bool
num = int(input("Nhập số: "))
if bool(num % 2):
    print("Đây là số lẻ")
else:
    print("Đây là số chẵn")
"""

"""
# Cách 11 dùng set
num = int(input("Nhập số: "))
print("Đây là số chẵn" if num % 2 in {0} else "Đây là số lẻ")
"""

"""
# Cách 12 dùng not
num = int(input("Nhập số: "))
if not num % 2:
    print("Đây là số chẵn")
else:
    print("Đây là số lẻ")
"""

"""
# Cách 13 dùng đệ quy
def is_even(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return is_even(n - 2)

num = int(input("Nhập số: "))
print("Đây là số chẵn" if is_even(num) else "Đây là số lẻ")
"""

"""
# Cách 14 dùng phép chia
num = int(input("Nhập số: "))
if num / 2 == int(num / 2):
    print("Đây là số chẵn")
else:
    print("Đây là số lẻ")
"""

"""
# Cách 1 cơ bản
age = int(input("Nhập tuổi của bạn: "))

if age < 13:
    print("Bạn là trẻ em")
elif age < 20:
    print("Bạn là thanh thiếu niên")
elif age < 60:
    print("Bạn là người trưởng thành")
else:
    print("Bạn là người cao tuổi")  
"""

"""
# Cách 2 dùng match-case (Python 3.10+)
age = int(input("Nhập tuổi: "))

match age:
    case a if a < 13:
        print("Trẻ em")
    case a if a < 20:
        print("Thanh thiếu niên")
    case a if a < 60:
        print("Người trưởng thành")
    case _:
        print("Người cao tuổi")
"""

"""
# Cách 3 dùng dictionary
age = int(input("Nhập tuổi: "))

groups = {
    age < 13: "Trẻ em",
    13 <= age < 20: "Thanh thiếu niên",
    20 <= age < 60: "Người trưởng thành",
    age >= 60: "Người cao tuổi"
}

print(groups[True])
"""

"""
# Cách 4 dùng hàm
def classify_age(age):
    if age < 13:
        return "Trẻ em"
    elif age < 20:
        return "Thanh thiếu niên"
    elif age < 60:
        return "Người trưởng thành"
    return "Người cao tuổi"

age = int(input("Nhập tuổi: "))
print(classify_age(age))
"""

"""
# Cách 5 dùng vòng lặp for
age = int(input("Nhập tuổi: "))

rules = [
    (age < 13, "Trẻ em"),
    (age < 20, "Thanh thiếu niên"),
    (age < 60, "Người trưởng thành"),
    (True, "Người cao tuổi")
]

for condition, label in rules:
    if condition:
        print(label)
        break
"""

"""
# Cách 6 dùng toán tử 3 ngôi lồng nhau
age = int(input("Nhập tuổi: "))
print("Trẻ em" if age < 13 else "Thanh thiếu niên" if age < 20 else "Người trưởng thành" if age < 60 else "Người cao tuổi")
"""

"""
# Cách 7 dùng dictionary và hàm min
age = int(input("Nhập tuổi: "))

groups = {
    13: "Trẻ em",
    20: "Thanh thiếu niên",
    60: "Người trưởng thành",
    float('inf'): "Người cao tuổi"
}

label = groups[min(k for k in groups if age < k)]
print(label)
"""

"""
# Cách 8 dùng bisect
import bisect

age = int(input("Nhập tuổi: "))

limits = [13, 20, 60]  
labels = ["Trẻ em", "Thanh thiếu niên", "Người trưởng thành", "Người cao tuổi"]

i = bisect.bisect(limits, age)
print(labels[i])
"""

"""
# Cách 9 dùng lambda và zip
age = int(input("Nhập tuổi: "))

rules = [
    lambda x: x < 13,
    lambda x: x < 20,
    lambda x: x < 60,
    lambda x: True
]

labels = ["Trẻ em", "Thanh thiếu niên", "Người trưởng thành", "Người cao tuổi"]

for rule, label in zip(rules, labels):
    if rule(age):
        print(label)
        break
"""

"""
# Cách 10 dùng filter và lambda
age = int(input("Nhập tuổi: "))

rules = [
    (lambda x: x < 13, "Trẻ em"),
    (lambda x: x < 20, "Thanh thiếu niên"),
    (lambda x: x < 60, "Người trưởng thành"),
    (lambda x: True, "Người cao tuổi")
]

print(list(filter(lambda r: r[0](age), rules))[0][1])
"""

"""
# Cách 11 dùng numpy (cần cài đặt thư viện numpy)
import numpy as np

age = int(input("Nhập tuổi: "))

bins = [0, 13, 20, 60, 200]
labels = ["Trẻ em", "Thanh thiếu niên", "Người trưởng thành", "Người cao tuổi"]

idx = np.digitize(age, bins) - 1
print(labels[idx])
"""

"""
# Cách 12 dùng pandas (cần cài đặt thư viện pandas)
import pandas as pd

age = int(input("Nhập tuổi: "))

bins = [0, 13, 20, 60, 200]
labels = ["Trẻ em", "Thanh thiếu niên", "Người trưởng thành", "Người cao tuổi"]

print(pd.cut([age], bins=bins, labels=labels)[0])
"""



# Nhập điểm
math = float(input("Nhập điểm Toán: "))
literature = float(input("Nhập điểm Văn: "))
english = float(input("Nhập điểm Anh: "))

# Tính điểm trung bình
avg = (math + literature + english) / 3
print("Điểm trung bình:", avg)

# Xếp loại
if avg >= 8.0:
    print("Xếp loại: Giỏi")
elif avg >= 6.5:
    print("Xếp loại: Khá")
elif avg >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu") 