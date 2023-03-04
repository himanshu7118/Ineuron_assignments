# 1.Write a Python Program to Display Fibonacci Sequence Using Recursion?
# Ans:

def recur(n):
  if n <= 1:
    return n
  else:
    return (recur(n-1) + recur(n-2))

nterm = 10

if nterm <= 0:
  print('provide positive int')
else:
  for i in range(nterm):
    print(recur(i))


# 2.Write a Python Program to Find Factorial of Number Using Recursion?
# Ans:

def fibo_cal(n):
  if n == 1:
      return n
  else:
      return n*fibo_cal(n-1)

print(fibo_cal(3))


# 3.Write a Python Program to calculate your Body Mass Index?
# Ans:

weight = 65 #write weight in kg

height = 5.2 #write height in meter

BMI = weight / height ** 2 

print(BMI)



# 4.Write a Python Program to calculate the natural logarithm of any number?
# Ans:

import math

# Return the natural logarithm of different numbers
print(math.log(2.7183))
print(math.log(2))
print(math.log(1))

# 5.Write a Python Program for cube sum of first n natural numbers?
# Ans:

n = 7

def cube_func(n):
  sum = 0
  for i in range(1,n+1):
    sum += i**3
  return sum

print(cube_func(2))

