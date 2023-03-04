# 1.	Write a Python program to Extract Unique values dictionary values?
# Ans:

dict1 = {
    "abc": 1,
    "xyz": 2,
    "hzy": 3,
    "cook" : 1,
    "fight": 2
}

def unique_value(dict1):
  values = []
  for i,j in dict1.items():
    if j in values:
      values.remove(j)
    else:
      values.append(j)
  return values

print(unique_value(dict1))


# 2.	Write a Python program to find the sum of all items in a dictionary?
# Ans:

dict1 = {
    "abc": 1,
    "xyz": 2,
    "hzy": 3,
    "cook" : 1,
    "fight": 2
}

def sum_items(dict1):
  sums = 0
  for i,j in dict1.items():
      sums = sums + j
  return sums

print(sum_items(dict1))


# 3.	Write a Python program to Merging two Dictionaries?
# Ans:

dict1 = {
    "abc": 1,
    "xyz": 2,
    "hzy": 3
}

dict2 = {
    "a":1,
    "b": 2
}

dict1.update(dict2)

print(dict1)


# 4.	Write a Python program to convert key-values list to flat dictionary?
# Ans:

test_dict = {
    'month' : [1, 2, 3],
    'name' : ['Jan', 'Feb', 'March']}

def convert_dict(test_dict):
  dict1 = {}
  list1 = list(test_dict.values())

  x = 0
  while x < len(list1[0]):
    dict1[list1[0][x]] = list1[1][x]
    x += 1

  return dict1

print(convert_dict(test_dict))


# 5.	Write a Python program to insertion at the beginning in OrderedDict?
# Ans:

from collections import OrderedDict
 
iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])
 
iniordered_dict.update({'manjeet':'3'})
iniordered_dict.move_to_end('manjeet', last = False)
 
print(iniordered_dict)


# 6.	Write a Python program to check order of character in string using OrderedDict()?
# Ans:

from collections import OrderedDict 
  
def checkOrder(input, pattern): 
      
    dict = OrderedDict.fromkeys(input) 

    ptrlen = 0
    for key,value in dict.items(): 
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
          
        if (ptrlen == (len(pattern))): 
            return 'true'

    return 'false'

print(checkOrder('engineers rock','ne'))


# 7.	Write a Python program to sort Python Dictionaries by Key or Value?
# Ans:

myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
 
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
 
print(sorted_dict)

