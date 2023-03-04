# 1.Write a Python Program to find sum of array?
# Ans:

x = [1,2,3,4,5,6,7,8,9]

def count_array(x):
  sum = 0
  for i in x:
    print(sum)
    sum = sum + i
  return sum

print(count_array(x))


# 2.Write a Python Program to find largest element in an array?
# Ans:

x = [1,2,3,4,5,6,7,8,9]

def lar_element(x):
  lar = 0
  for i in range(len(x)):
    try:
      if x[i] >= x[i+1]:
        lar = x[i]
      else:
        lar = x[i+1]
    except:
      pass
  return lar

#or in other way 

def lar_element(x):
  lar = x[0]
  for i in range(1,len(x)):
    if x[i] > lar:
      lar = x[i]
  return lar

print(lar_element(x))


# 3.Write a Python Program for array rotation?
# Ans:

x = [1,2,3,4,5,6,7,8,9]

def rota_arr(x,n,ro):
  temp = []
  i = 0
  while ro > i:
    temp.append(x[i])
    i += 1

  i = 0
  while (ro < n):
    x[i] = x[ro]
    i += 1
    ro += 1

  final_res = x + temp

  return final_res

print(rota_arr(x,len(x),2))


# 4.Write a Python Program to Split the array and add the first part to the end?
# Ans:

x = [1,2,3,4,5,6,7,8,9]

def split_func(x,y):
  temp = []
  i = 0
  while y > i:
    temp.append(x[i])
    i += 1

  for j in temp:
    x.remove(j)

  final_res = x + temp

  return final_res

print(split_func(x,4))

# 5.Write a Python Program to check if given array is Monotonic?
# Ans:

x = [5,6,8,2]

y = [2,3,4,5]

z = [5,4,3,2]

def mono_func(n):
  i = 0
  res = ''
  j = 0
  while j < len(n) - 1:
    if n[i] >= n[i+1]:
      i+=1
      if res == 'less':
        return False
      res = 'greater'
    elif n[i] <= n[i+1]:
      i+=1
      if res == 'greater':
        return False
      res = 'less'
    j += 1
  return True

print(mono_func(z))
print(mono_func(x))
print(mono_func(y))

