# Question 1:

# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# Ans:

def generator(n):
    list_of = range(1,n+1)
    for i in list_of:
        if i % 7 == 0:
            yield i

print(list(generator(40)))


# Question 2:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 

# Suppose the following input is supplied to the program:

# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:

# 2:2

# 3.:1

# 3?:1

# New:1

# Python:5

# Read:1

# and:1

# between:1

# choosing:1

# or:2

# to:1
# Ans:

str1 = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

def sorted_str(str1):
  list1 = str1.split(" ")
  dict1 = {}
  for i in list1:
    if i in dict1:
      dict1[i] = dict1[i] + 1
    else:
      dict1[i] = 1
  return dict1
    
  print(list1)

print(sorted_str(str1))


# Question 3:
# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
# Ans:

class Person(object):
    def __init__(self):
      self.gender = "unknown"

    def getGender(self):
      print(self.gender)

class Male(Person):
    def __init__(self):
      self.gender = "Male"

class Female(Person):
    def __init__(self):
      self.gender = "Female"

jeel = Female()
himanshu = Male()
himanshu.getGender()
jeel.getGender()


# Question 4:
# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
# Ans:

subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]

for sub in subjects:
    for verb in verbs:
        for obj in objects:
            print("{} {} {}".format(sub,verb,obj))



# Question 5:
# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
# Ans:

import zlib
s = 'hello world!hello world!hello world!hello world!'
y = bytes(s, 'utf-8')
t = zlib.compress(y)
print(t)
print(zlib.decompress(t))


# Question 6:
# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
# Ans:

lst = [1,3,5,7]
item = 5

def binary_search(list1,item):
  low = 0
  high = len(list1) - 1

  while low < high:
    for i in list1:
      if i == item:
        return low
      else:
        low += 1
  return low

print(binary_search(lst,item))
