# 1.Write a Python Program to Add Two Matrices?
# Ans:

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[11,12,13],
     [14,15,16],
     [17,18,19]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(A)):
  for j in range(len(A[i])):
    result[i][j] = A[i][j] + B[i][j] 

print(result)


# 2.Write a Python Program to Multiply Two Matrices?
# Ans:

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[11,12,13],
     [14,15,16],
     [17,18,19]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(A)):
  for j in range(len(A[i])):
    result[i][j] = A[i][j] * B[i][j]

print(result)


# 3.Write a Python Program to Transpose a Matrix?
# Ans:

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(A)):
  for j in range(len(A[i])):
    result[j][i] = A[i][j]

print(result)


# 4.Write a Python Program to Sort Words in Alphabetic Order?
# Ans:
my_str = "Hye this example of sorting given by himanshu"

words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are:")
for word in words:
   print(word)


# 5.Write a Python Program to Remove Punctuation From a String?
# Ans:

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hye this example of 'sorting' <given> by himanshu"

no_punc = ""

for word in my_str:
   if word not in punctuations:
     no_punc = no_punc + word

print(no_punc)
