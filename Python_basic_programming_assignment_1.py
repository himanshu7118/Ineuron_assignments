# 1.Write a Python program to print "Hello Python"?
# Ans:

print('Hello Python')


# 2.Write a Python program to do arithmetical operations addition and division.?
# Ans:

a = 2
b = 6

print(a+b)
print(a-b)


# 3.Write a Python program to find the area of a triangle?
# Ans:

a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
s = (a + b + c) / 2  
  
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(area)


# 4.Write a Python program to swap two variables?
# Ans:

a = 2

b = 6

c = a 

a = b

b = c

print(a)
print(b)


# 5. Write a Python program to generate a random number?
# Ans:

import random

print(random.randint(0,9))
