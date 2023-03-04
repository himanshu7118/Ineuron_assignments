# 1.Write a Python Program to Find LCM?
# Ans:

num1 = 12
num2 = 14 

if num1 > num2:
  greater = num1
else:
  greater = num2

while(True):
  if (greater % num1 == 0) and (greater % num2 == 0):
    Lcm = greater
    break 
  greater += 1

print(Lcm)


# 2.Write a Python Program to Find HCF?
# Ans:

num1 = 12
num2 = 24

if num1 < num2:
  smaller = num1
else:
  smaller = num2

for i in range(2,smaller+1):
  if (num1 % i == 0) and (num2 % i == 0):
    hcf = i

print(hcf)


# 3.Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
# Ans:

dec = 344
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# 4.Write a Python Program To Find ASCII value of a character?
# Ans:

c = 'p'
print("The ASCII value of" + c + "is", ord(c))


# 5.Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
# Ans:

x = 10 
y = 12

def add(x,y):
  return x + y

def mul(x,y):
  return x * y

def divi(x,y):
  return x / y

def sub(x,y):
  return x - y

print('addition',add(x,y))
print('subtraction',sub(x,y))
print('multiplication',mul(x,y))
print('division',divi(x,y))
