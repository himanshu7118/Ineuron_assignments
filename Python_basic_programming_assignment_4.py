# 1.Write a Python Program to Find the Factorial of a Number?
# Ans:

x = 5

y = 1

for i in range(1,x+1):
  y = y * i

print(y)


# 2.Write a Python Program to Display the multiplication Table?
# Ans:

x = 9

for i in range(1,11):
  print(f'{x} x {i} = {x * i}')



# 3.Write a Python Program to Print the Fibonacci sequence?
# Ans:

xyz = []

x,y = 0,1

nth = 10

count = 0

while count < nth:
  xyz.append(x)
  cal = x + y
  x = y
  y = cal
  count += 1

print(xyz)


# 4.Write a Python Program to Check Armstrong Number?
# Ans:

x = 153
y = []

for i in str(x):
  y.append(i)

temp = 0

for b in y:
  temp = temp + int(b)**3

if x == temp:
  print(f'{x} is Armstrong Number')
else:
  print(f'{x} is not Armstrong Number')



# 5.Write a Python Program to Find Armstrong Number in an Interval?
# Ans:

ans = []

for i in range(100,1001):
  y = []
  for j in str(i):
    y.append(j)
  temp = 0
  for b in y:
    temp = temp + int(b)**3
  if i == temp:
    ans.append(i)
  else:
    pass

print(ans)


# 6.Write a Python Program to Find the Sum of Natural Numbers?
# Ans:

num = 16

sum = 0

while num >0:
  sum = sum + num
  num -= 1

print(sum)
