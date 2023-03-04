
# 1.Write a Python program to convert kilometers to miles?
# Ans:

km = 144

def convert_km(km):
  x = km/2
  y = x/4
  miles = x + y
  return int(miles)

print(convert_km(km))


# 2.Write a Python program to convert Celsius to Fahrenheit?
# Ans:

c = 12

F = c * 1.8000+ 32.00

print(F)


# 3.Write a Python program to display calendar?
# Ans:

import calendar

yy = 2022 
mm = 12   

print(calendar.month(yy, mm))


# 4.Write a Python program to solve quadratic equation?
# Ans:

import cmath

a = 4
b = 6
c = 8

dis = (b**2) - (4 * a*c)

ans1 = (-b-cmath.sqrt(dis))/(2 * a)
ans2 = (-b + cmath.sqrt(dis))/(2 * a)

print(ans1)
print(ans2)


# 5.Write a Python program to swap two variables without temp variable?
# Ans:

x = 4
y = 3

x,y = y,x

print(x)
print(y)
