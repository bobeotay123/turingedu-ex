import math
# Nhập số nguyên n. Nếu n là số lẻ thì in ra "hello, world!"
n = int(input("n = "))
if n % 2 != 0:
    print("hello, world!")

# Nhập số nguyên dương n. Nếu n là số chính phương thì in ra "n là số chính phương"
n = int(input("n = "))
n_sqrt = int(math.sqrt(n))
if n == n_sqrt * n_sqrt:
    print(n + "là số chính phương")

# nhập 2 số thực, in ra số lớn hơn
a = float(input("a = "))
b = float(input("b = "))
if a < b:
    a = b
print(a)

# nhập số thực n. hãy in ra giá trị tuyệt đối của n
n = float(input("n = "))
absoluteValue = n
if n < 0:
    absoluteValue = -1.0 * n

print(f"|{n}| = {absoluteValue}")

# Nhập vào 1 năm bất kỳ. Nếu năm đó là năm nhuận thì in ra "NHUAN"
year = int(input("Enter a random year: "))
if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print("NHUAN")

# Nhập vào ba số thực a, b, c. Nếu a, b, c tạo thành 3 cạnh của 1 tam giác thì in ra "TRIANGLE"
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a > 0 and b > 0 and c > 0 and (a + b > c or b + c > a or a + c > b):
    print("TRIANGLE")

# Nhập 3 số thực a, b, c. In ra 3 số theo thứ tự giảm dần
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a < b:
    tmp = b
    b = a
    a = tmp
if a < c:
    tmp = c
    c = a
    a = tmp
if b < c:
    tmp = b
    b = c
    c = tmp
print("Dãy số sau khi sắp xếp: ", a, b, c)
