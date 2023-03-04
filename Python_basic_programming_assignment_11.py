# 1.	Write a Python program to find words which are greater than given length k?
# Ans:

words = "Hye I am Himanshu Rami"

def find_word(words,N):
  list1 = words.split(' ')
  greater_word = []
  for i in list1:
    if len(i) > N:
      greater_word.append(i)
  return greater_word

print(find_word(words,3))


# 2.	Write a Python program for removing i-th character from a string?
# Ans:

string1 = "HyehelloWhy"

def reove_ith(string1,N):
  a = string1[:N]
  b = string1[N+1:]

  return a+b

print(reove_ith(string1,5))


# 3.	Write a Python program to split and join a string?
# Ans:

words = "Hye I am Himanshu Rami"

def find_word(words,N):
  list1 = words.split(' ')
  data1 = " ".join(list1)
  return data1

print(find_word(words,3))


# 4.	Write a Python to check if a given string is binary string or not?
# Ans:

data = '2030213103'

def check_binary(data):
  j = 0
  for i in data:
    if i == '0':
      if data[j+1] == '1':
        return "Its binary string"
      j += 1
    else:
      j += 1
  return "Its not binary string"

print(check_binary(data))


# 5.	Write a Python program to find uncommon words from two Strings?
# Ans:

str1 = "Geeks for Geeks"
str2 = "Learning from Geeks for Geeks"

def unmatch_word(str1,str2):
  data1 = str1.split(' ')
  data2 = str2.split(' ')
  comman_words = {}
  for word in data1:
    comman_words[word] = comman_words.get(word, 0) + 1
  for word in data2:
    comman_words[word] = comman_words.get(word, 0) + 1

  return [i for i,j in comman_words.items() if j == 1]

print(unmatch_word(str1,str2))


# 6.	Write a Python to find all duplicate characters in string?
# Ans:

str1 = 'Abchdbfffkieuqba'

def duplicate_char(str1):
  ex = []
  dup1 = []
  for i in str1:
    if i in ex:
      dup1.append(i)
    else:
      ex.append(i)
  dup1 = list(set(dup1))
  return dup1

print(duplicate_char(str1))


# 7.	Write a Python Program to check if a string contains any special character?
# Ans:

str1 = 'Ab[chdbfff)k<ieu>q}ba'

def spec_char(str1):
  s='[@_!#$%^&*()<>?/\|}{~:]'
  spec = []
  for x in s:
    if x in str1:
      spec.append(x)

  return spec

print(spec_char(str1))
