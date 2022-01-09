import math

# Nhập vào hai số nguyên a, b (a < b). Hãy đếm số số chẵn, số lẻ trong đoạn [a;b]
a = int(input('a = '))
b = int(input('b = '))
odd = 0
even = 0
for i in range(a, b + 1):
    if i % 2:
        odd += 1
    else:
        even += 1
print(f"Trong đoạn [{a};{b}] có {odd} số lẻ và {even} số chẵn")


# Nhập số nguyên n. Xác định n có phải số nguyên tố không
n = int(input('n = '))
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")

# Liệt kê các số chính phương (khai căn nguyên) trong khoảng [a; b]
a = int(input('a = '))
b = int(input('b = '))
for i in range(int(math.sqrt(a)), int(math.sqrt(b)) + 1):
    if i * i < a:
        continue
    print(i * i, end=' ')

# In ra số fibonacci thứ n (n > 0)
n = int(input('n = '))
fibonacci = 1
prev_fib1 = 1
prev_fib2 = 1
if n > 2:
    for i in range(2, n):
        fibonacci = prev_fib1 + prev_fib2
        prev_fib2 = prev_fib1
        prev_fib1 = fibonacci
print(f"fibonacci({n}) = {fibonacci}")

# Nhập n (n > 0). Tính biểu thức
'''
  - S1 = n giai thừa 
  - S2 = 1^2 + 2^2 + … + n^2 
  = S3 = 1 + 1/(1+2) + 1/(1+2+3) + 1/(1+2+3+4) + … + 1/(1+2+3+4+…+n) 
'''
n = int(input('n = '))
S1 = 1
S2 = 0
S3 = 0
s_tmp = 1

for i in range(2, n + 1):
    # n!(n > 0)
    S1 *= i
    # Tổng các bình phương
    S2 += i * i
    # S3
    s_tmp += i
    S3 += 1 / s_tmp

print(f"S1 = {S1}\nS2 = {S2}\nS3 = {S3}")
