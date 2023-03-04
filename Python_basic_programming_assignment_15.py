# Question 1:
# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 100
# Then, the output of the program should be:
# 0,35,70
# Ans:

def genrator_func(n):
  for i in range(n+1):
    if i % 7 == 0 or i % 5 == 0:
      yield str(i)

data1 = list(genrator_func(100))

str1 = ",".join(data1)

print(str1)


# Question 2:
# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10
# Ans:

def genrator_func(n):
  for i in range(n+1):
    if i % 2 == 0:
      yield str(i)

data1 = list(genrator_func(10))

str1 = ",".join(data1)

print(str1)


# Question 3:
# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
# Example:
# If the following n is given as input to the program:
# 7

# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13
# Ans:

def fibonaci(n):
    a = 0
    b = 1
    list1 = []
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
      x = [0,1]
      mylist = [x.append(x[i-2]+x[i-1]) for i in range(2,n+1)]
      str1 = ','.join([str(i) for i in x])
      return str1
 
print(fibonaci(7))


# Question 4:
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# John
# Ans:

def comprresed_lettr(n):
  data1 = n.split('@')
  return data1[0]

print(comprresed_lettr('john@google.com'))


# Question 5:
# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
# Ans:

class Square:

  def __init__(self,len):
    self.len = len

  def area(self):
    return self.len

class Shape():

  def area(self):
    return 0

sq = Square(20)
len = sq.len
s = Shape()
print(sq.area())
print(s.area())
