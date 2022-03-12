import math

# Viết chương trình nhập vào n số thực và đưa ra số nhỏ nhất, lớn nhất
n = int(input('n = '))

while n < 2:
  print("n > 2 !")
  n = int(input('n = '))

smallest_number = 0
greatest_number = 0

for i in range(n):
  x = int(input())
  if i:
    if x > greatest_number:
      greatest_number = x
    if x < smallest_number:
      smallest_number = x
  else:
    greatest_number = x
    smallest_number = x

print("Số nhỏ nhất:", smallest_number)
print("Số lớn nhất:", greatest_number)


# Viết chương trình vẽ một tam giác vuông cân rỗng cạnh height (nguyên dương) bằng các dấu bằng 1 kí tự ASCII do người dùng nhập.
character = input("Kí tự để vẽ tam giác: ")
height = int(input("Nhập kích thước tam giác: "))

for i in range(height):
  for _ in range(i + 1):
    print(character, end="")
  print('') 


# Viết chương trình phân tích một số nguyên n thành tích của các thừa số nguyên tố.

n = int(input("n = "))
n_copy = n
print(n_copy, '=', end=' ')
for i in range(2, n):
  power = 0
  while n % i == 0:
    power += 1
    n = n / i
  if power > 0:
    if power > 1:
      print(i, "^", power, sep='', end=' ')
    else:
      print(i, end=' ')
    if n == 1:
      break
    else:
      print("*", end=' ')
    
if n > 1:
  print(n) 


# Viểt chương trình kiểm tra xem số tự nhiên n có phải số hoàn thiện hay không
# (số hoàn thiện là số có tổng các ước nguyên dương bằng chính nó)

n = int(input("n = "))
sum = 0
for i in range(1, int(n / 2) + 1):
  if sum > n:
    break
  if n % i == 0:
    sum += i

if sum == n:
  print(n, "là số hoàn thiện")
else:
  print(n, "không phải là số hoàn thiện")


# Viết chương trình in ra các số nguyên tố trong khoảng từ l đến r 
# (l, r là số nguyên dương; r - l <= 200)
l = int(input('l = '))
r = int(input('r = '))

for i in range(l, r + 1):
  if i < 2:
    pass
  isPrime = True
  for j in range(2, int(math.sqrt(i)) + 1):
    if i % j == 0:
      isPrime = False
      break
  if isPrime:
    print(i, end=' ')


#	Viết chương trình nhập vào số nguyên dương n (n < 10) rồi tính tổng: n + nn + nnn +...+ nn…n 
# (số hạng cuối gồm n chữ số n)
n = int(input("n = "))
n_copy = n
sum = 0

for i in range(n):
  sum += n_copy
  n_copy = n_copy * 10 + n

print(sum)


# Viết chương trình tìm ước số chung lớn nhất và bội số chung nhỏ nhất của 2 số nguyên.
a = int(input("a = "))
b = int(input("b = "))

if a < b:
  tmp = a
  a = b
  b = tmp

gcd = a 

while a*b != 0:
  gcd = gcd % b
  if gcd < b:
    temp = b
    b = gcd
    gcd = temp

lcm = int(a * b / gcd)

print("UCLN:", gcd)
print("BCNN:", lcm)
