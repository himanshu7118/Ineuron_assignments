# 1.Write a Python program to find sum of elements in list?
# Ans:

list_data = [1,2,3,4,5,6,7,8,9]

list_ans = 0

for i in list_data:
  list_ans = list_ans + i

print(list_ans)


# 2.Write a Python program to  Multiply all numbers in the list?
# Ans:

list_data = [1,2,3,4,5,6,7,8,9]

list_ans = 1

for i in list_data:
  list_ans = list_ans * i

print(list_ans)


# 3.Write a Python program to find smallest number in a list?
# Ans:

list_data = [1,2,3,4,5,6,7,8,9]

list_data.sort()
  
print(f"{list_data[0]} is small number in the list")

# or 

def find_small(n):
  small = n[0]
  for i in range(len(n)):
    if n[i] < small:
      small = n[i]

  return f"{small} is the smallest number in the list"

print(find_small(list_data))



# 4.Write a Python program to find largest number in a list?
# Ans:

list_data = [10,2,3,4,13,6,17,8,9]

def find_max(n):
  max = n[0]
  for i in range(len(n)):
    if n[i] > max:
      max = n[i]

  return f"{max} is the largest number in the list"

print(find_max(list_data))


# 5.Write a Python program to find second largest number in a list?
# Ans:

list_data = [10,2,3,4,13,6,17,8,9]

list_data.sort(reverse= True)

print(list_data[1])


# 6.Write a Python program to find N largest elements from a list?
# Ans:
def Nmaxelements(list1,N):
  max = list1[0]
  max_list = []
  i = 1
  while i <= N:
    for j in range(0,len(list1)):
      if list1[j] > max:
        max = list1[j]
    list1.remove(max)
    max_list.append(max)
    max = list1[0]
    i += 1

  return max_list

list1 = [12,25,84,13,12,19,49]
N = 3

print(Nmaxelements(list1,N))


# 7.Write a Python program to print even numbers in a list?
# Ans:

list1 = [12,25,84,13,12,19,49]

def even_func(list1):
  even = []
  for i in range(len(list1)):
    if list1[i] % 2 == 0:
      even.append(list1[i])

  return even

print(even_func(list1))


# 8.Write a Python program to print odd numbers in a List?
# Ans:

list1 = [12,25,84,13,12,19,49]

def odd_func(list1):
  odd = []
  for i in range(len(list1)):
    if list1[i] % 2 != 0:
      odd.append(list1[i])

  return odd

print(odd_func(list1))


# 9.Write a Python program to Remove empty List from List?
# Ans:

list1 = [1,2,3,[],6,[],10,[],99]

def remove_list(list1):
  for i in range(len(list1)):
    try:
      if list1[i] == []:
        list1.remove(list1[i])
    except Exception:
      break
  return list1

print(remove_list(list1))


# 10.Write a Python program to Cloning or Copying a list?
# Ans:

def clonning(list1):
  list2 = list1
  return list2

list1 = [12,25,84,13,12,19,49]
list2 = clonning(list1)

print(list1)
print(list2)


# 11.Write a Python program to Count occurrences of an element in a list?
# Ans:

list1 = [12,25,84,13,12,19,49]
N = 12

def count_rept(list1,N):
  count = 0
  for i in list1:
    if i == N:
      count += 1

  return count

print(count_rept(list1,N))
