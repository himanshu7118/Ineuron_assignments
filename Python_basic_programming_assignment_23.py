# Question 1
# Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.
# Examples
# is_symmetrical(7227) ➞ True

# is_symmetrical(12567) ➞ False

# is_symmetrical(44444444) ➞ True

# is_symmetrical(9939) ➞ False

# is_symmetrical(1112111) ➞ True
# Ans:

def check_func(num):
  revs_number = 0 
  number = num 
  
  while (number > 0):  
      remainder = number % 10  
      revs_number = (revs_number * 10) + remainder  
      number = number // 10  

  if num == revs_number:
    return True
  else:
    return False

print(check_func(12567))
print(check_func(44444444))

  
# Question 2
# Given a string of numbers separated by a comma and space, return the product of the numbers.
# Examples
# multiply_nums("2, 3") ➞ 6

# multiply_nums("1, 2, 3, 4") ➞ 24

# multiply_nums("54, 75, 453, 0") ➞ 0

# multiply_nums("10, -2") ➞ -20
# Ans:

def multiply_nums(s):
    s = s.replace(' ', "")
    s = s.split(',')
    sum = 1
    for i in s:
        sum = sum * int(i)
    return sum

# Question 3
# Create a function that squares every digit of a number.
# Examples
# square_digits(9119) ➞ 811181

# square_digits(2483) ➞ 416649

# square_digits(3212) ➞ 9414
# Notes
# The function receives an integer and must return an integer.
# Ans:

def square_digits(num):
  data = ''.join(str(int(i) ** 2) for i in str(num))
  return data

print(square_digits(9119))


# Question 4
# Create a function that sorts a list and removes all duplicate items from it.
# Examples
# setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]

# setify([4, 4, 4, 4]) ➞ [4]

# setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]

# setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]
# Ans:

def setify(lst):
    return list(set(lst))

print(setify([1, 3, 3, 5, 5]))

# Question 5
# Create a function that returns the mean of all digits.
# Examples
# mean(42) ➞ 3

# mean(12345) ➞ 3

# mean(666) ➞ 6
# Notes
# • The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
# • The mean will always be an integer.
# Ans:

def mean(n):
  N = len(str(n))
  sum = 0
  for i in str(n):
    sum += int(i)

  return int(sum/N)

print(mean(42))
print(mean(12345))
print(mean(666))

