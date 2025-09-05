# for i in range(1, 11):
#     print(i)

# for i in range(2, 21, 2):
#     print(i)

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# i = 2
# while i <= 20:
#     print(i)
#     i += 2

# number = [2, 4, 6, 8, 10]
# for i in number:
#     print(i)

# for i in range(1, 11):
#     print(i * 2)

# def print_even(n):
#     if n > 20:   # điều kiện dừng
#         return
#     print(n)
#     print_even(n + 2)  # gọi lại chính nó với số tiếp theo

# print_even(2)

# list(map(lambda x: print(x), [2*i for i in range(1, 11)]))


# def even_numbers():
#     n = 2
#     while n <= 20:
#         yield n
#         n += 2

# for num in even_numbers():
#     print(num)

# for x in [2 * i for i in range(1, 11)]:
#     print(x)

# tong = 0                      # ❶ khởi tạo biến tổng ban đầu
# for i in range(1, 101):       # ❷ lặp qua các số từ 1 đến 100
#     tong += i                 # ❸ cộng dồn vào biến tổng
# print("Tổng từ 1 đến 100 là:", tong)   # ❹ in kết quả

# n = 100000000000
# tong = n * (n + 1) // 2
# print("Tổng từ 1 đến 100 là:", tong)

# n = 100000

# tong = n * (n + 1) // 2

# print("Tổng từ 1 đến", n, "là:", tong)

# for n in range(1, 11):
#     if n % 2 == 0:
#         print(f"{n} là số chẵn")
#     else:
#         print(f"{n} là số lẻ")

# so_list = [int(x) for x in input("Nhập các số, cách nhau bởi khoảng trắng: ").split()]
# for n in so_list:
#     if n % 2 == 0:
#         print(f"{n} là số chẵn")
#     else:
#         print(f"{n} là số lẻ")

# n = int(input("Nhập một số: "))
# check = {True: "Số chẵn", False: "Số lẻ"}
# print(check[n % 2 == 0])

# def chan_le(n):
#     return "Số chẵn" if n % 2 == 0 else "Số lẻ"

# # Chỉ cần gọi hàm nhiều lần

# i = int(input("Nhập một số: "))
# print(chan_le(i))

# print([f"{n} là số {'chẵn' if n % 2 == 0 else 'lẻ'}" for n in map(int, input("Nhập các số (cách nhau bởi khoảng trắng): ").split())])

# n = int(input("Nhập một số cần in bảng cửu chương: "))

# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# for n in range(1, 10):
#     print(f"\nBảng cửu chương {n}:")
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n*i}")

# n = int(input("Nhập n: "))
# tong = 0
# for i in range(1, n+1):
#     tong += i
# print("Tổng từ 1 đến", n, "là:", tong)

# n = int(input("Nhập n: "))
# tong = n * (n + 1) // 2
# print("Tổng từ 1 đến", n, "là:", tong)

# n = int(input("Nhập một số: "))
# print("Số chẵn" if n % 2 == 0 else "Số lẻ")

for i in range(1, 11):
    print(f"7 x {i} = {7*i}")
