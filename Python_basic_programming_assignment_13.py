# Question 1:

# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 * C * D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.

# Example

# Let us assume the following comma separated input sequence is given to the program:

# 100,150,180

# The output of the program should be:

# 18,22,24
# Ans:

import math

def test_func(data):
  c = 50
  h = 30
  value = []
  items=[x for x in data.split(',')]
  for d in items:
      value.append(str(round(math.sqrt(2*c*float(d)/h))))

  str1 = ','.join(value)
  return str1

print(test_func(input("Enter a values in coma seprated form: ")))


# Question 2:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

# Note: i=0,1.., X-1; j=0,1,¡¬Y-1.

# Example

# Suppose the following inputs are given to the program:

# 3,5

# Then, the output of the program should be:

# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
# Ans:

i = int(input("Enter value of i: "))
j = int(input("Enter value of j: "))

def create_array(i,j):
  col = []
  row = []
  temp = 0
  tempy = 0
  for x in range(0,i):
    for y in range(0,j):
      if temp == 1:
        row.append(y)
      elif temp > 1:
        row.append(tempy)
        tempy += 2 
      else:
        row.append(temp)
    temp += 1
    col.append(row)
    row = []
  return col

print(create_array(i,j))



# Question 3:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

# Suppose the following input is supplied to the program:

# without,hello,bag,world

# Then, the output should be:

# bag,hello,without,world
# Ans:

inputdata = str(input("Enter comma seprated words: "))

array = inputdata.split(',')

array.sort()

data = ','.join(array)

print(data)

# Question 4:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

# Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again

# Then, the output should be:

# again and hello makes perfect practice world
# Ans:

inputdata = str(input("Enter whitespace seprated words: "))

array = inputdata.split(' ')

array.sort()

array = list(set(array))

data = ' '.join(array)

print(data)


# Question 5:
# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123

# Then, the output should be:

# LETTERS 10

# DIGITS 3
# Ans:

import string

special_chars = string.punctuation

inputdata = str(input("Enter words: "))

array = inputdata.split(' ')

define_digits = '1234567890'

letters = 0
digits = 0

for i in array:
  for j in i:
    if type(j)  == str and j not in special_chars and j not in define_digits:
      letters += 1
    elif j in define_digits:
      digits += 1

print(letters)
print(digits)


# Question 6:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

# Following are the criteria for checking the password:

# 1. At least 1 letter between [a-z]

# 2. At least 1 number between [0-9]

# 1. At least 1 letter between [A-Z]

# 3. At least 1 character from [$#@]

# 4. Minimum length of transaction password: 6

# 5. Maximum length of transaction password: 12

# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

# Example

# If the following passwords are given as input to the program:

# ABd1234@1,a F1#,2w3E*,2We3345

# Then, the output of the program should be:

# ABd1234@1
# Ans:

import re
import string

special_chars = string.punctuation

x = input("Enter Username:")
y = input("Enter Password:")

passwords = y.split(",")

accepted_pass = []
for i in passwords:
    
    if len(i) < 6 or len(i) > 12:
        continue

    elif not re.search("([a-z])+", i):
        continue

    elif not re.search("([A-Z])+", i):
        continue

    elif not re.search("([0-9])+", i):
        continue

    elif not re.search("([!@$%^&])+", i):
        continue

    else:
        accepted_pass.append(i)

print((" ").join(accepted_pass))

