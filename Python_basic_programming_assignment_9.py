# 1.Write a Python program to check if the given number is a Disarium Number?
# Ans:

def check(n):
  length = 0
  while (n != 0):
    length = length +1
    n = n//10
  return length

def dis_fuc(n):
  length = check(n)
  y = 1
  ans = 0
  for i in str(n):
    if not y > length:
      ans = ans + int(i)**y
      y = y + 1
  if ans == int(n):
    return f"{n} Its Disarium Number"
  else:
    return f"{n} Its not Disarium Number"

print(dis_fuc(189))


# 2.Write a Python program to print all disarium numbers between 1 to 100?
# Ans:

def check(n):
  length = 0
  while (n != 0):
    length = length +1
    n = n//10
  return length

def dis_fuc():
  Disarium = []
  for i in range(1,100):
      length = check(i)
      y = 1
      ans = 0
      for j in str(i):
        if not y > length:
          ans = ans + int(j)**y
          y = y + 1
      if ans == int(i):
        Disarium.append(ans)
  return f"{Disarium} its a Disarium number in range 1-100"

print(dis_fuc())


# 3.Write a Python program to check if the given number is Happy Number?
# Ans:

def isHappynumber(n):
    if n == 1 or n == 7:
        return True
          
    Sum, x = n, n
  
    while Sum > 9:
        Sum = 0
          
        while x > 0:
            d = x % 10
            Sum += d * d
            x = int(x / 10)
         
        if Sum == 1:
            return True

        print(x,'after wile')
              
        x = Sum
     
    if Sum == 7:
        return True
          
    return False
 
n = 66
      
if isHappynumber(n):
    print(n, "is a Happy number")
else:
    print(n, "is not a Happy number")


# 4.Write a Python program to print all happy numbers between 1 and 100?
# Ans:

def isHappynumber(n):
    if n == 1 or n == 7:
        return True
          
    Sum, x = n, n
  
    while Sum > 9:
        Sum = 0
          
        while x > 0:
            d = x % 10
            Sum += d * d
            x = int(x / 10)
         
        if Sum == 1:
            return True
              
        x = Sum
     
    if Sum == 7:
        return True
          
    return False
 
n = 66

h = 0

happy_number = []

while h <= 100:      
  if isHappynumber(h):
      happy_number.append(h)
      h += 1
  else:
    h += 1
    pass

print(happy_number)


# 5.Write a Python program to determine whether the given number is a Harshad Number?
# Ans:

n = 20

def harsh_func(n):
  j = 0
  for i in str(n):
    j = j + int(i)

  if n % j == 0:
    return f"{n} is harshed number"
  else:
    return f"{n} is not harshed number"

print(harsh_func(n))


# 6.Write a Python program to print all pronic numbers between 1 and 100?
# Ans:

def pronic():
  i = 0
  j = 0
  pronic_list = []
  while j <= 100:
    j = i * (i + 1)
    if j <= 100:
      pronic_list.append(j)
    i += 1
  return pronic_list

print(pronic())
