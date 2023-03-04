# 1.Write a Python Program to Check if a Number is Positive, Negative or Zero?
# Ans:

x = 0

def check_num(x):
  if x > 0:
    return "Positive"
  elif x < 0:
    return "Negative"
  else:
    return "Zero"

print(check_num(x))

# 2.Write a Python Program to Check if a Number is Odd or Even?
# Ans:

x = 3

def check_num(x):
  if x%2 != 0:
    return "Odd"
  else:
    return "Even"

print(check_num(x))


# 3.Write a Python Program to Check Leap Year?
# Ans:

x = 2022

def check_year(x):
  if x%4 == 0:
    return "Leap year"
  else:
    return "Not Leap year"

print(check_year(x))


# 4.Write a Python Program to Check Prime Number?
# Ans:

x = 9

if x > 0:
  for i in range(2,x):
    if x%i == 0:
      print(x,'is not prime number')
      break
  else:
    print(x,'is prime number')


# 5.Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
# Ans:

list_prime = []

for num in range(10000):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           list_prime.append(num)

print(list_prime)

