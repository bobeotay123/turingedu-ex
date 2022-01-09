import math

# Viết chương trình xét xem một tam giác có là tam giác cân hay không khi biết ba cạnh của tam giác.
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == b or b == c or a == c:
    print("Tam giác cân")
else:
    print("Không phải Tam giác cân")

# Nhập vào giờ, phút, giây. Kiểm tra xem giờ, phút, giây có hợp lệ không
hour = int(input("Nhập giờ: "))
if 0 <= hour <= 24:
    minute = int(input("Nhập phút: "))
    if 0 <= minute <= 60:
        second = int(input("Nhập giây: "))
        if 0 <= second <= 60:
            print(f"Thời gian vừa nhập: {hour}h:{minute}m:{second}s")
        else:
            print("Giây không hợp lệ")
    else:
        print("Phút không hợp lệ")
else:
    print("Giờ không hợp lệ")

""" 
Viết chương trình nhập 3 số nguyên a, b, c:
  - Kiểm tra điều kiện 0 < a, b, c < 10
  - Nếu thỏa mãn điều kiện, in ra số tự nhiên lớn nhất tạo thành bằng cách ghép 3 số trên
"""
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if 0 < a < 10 and 0 < b < 10 and 0 < b < 10:
    if a < b:
        tmp = a
        a = b
        b = tmp
    if a < c:
        tmp = a
        a = c
        c = tmp
    if b < c:
        tmp = b
        b = c
        c = tmp
    print(f"Số lớn nhất tạo được: {a}{b}{c}")
else:
    print("Nhập không hợp lệ")

'''
Nhập vào phương trình bậc 2 ax^2 + bx + c : 
  - Xác định phương trình có nghiệm không
  - In ra nghiệm (nếu có)
'''
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print("Phương trình có nghiệm duy nhất: x =", x)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -1 * b / 2 * a
        print("Phương trình có nghiệm duy nhất: x =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phương trình có 2 nghiệm: x1 = ", x1, ", x2 = ", x2)

'''
Viết chương trình tính cước taxi biết 
    + Km đầu tiên 15 nghìn vnd 
    + 20 km tiếp theo 12 nghìn vnd 
    + Tiếp theo, 10 nghìn vnd / km 
'''
distance = float(input("Nhập quãng đường: "))
if distance > 0:
    price = 15
    if distance > 1:
        price += 12
        if distance > 20:
            price += int(10 * (distance - 20))
    print(f"Tổng tiền: {price},000VND")
else:
    print("Độ dài quãng đường phải lớn hơn 0")
