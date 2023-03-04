# Question1. Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.
# Examples
# evenly_divisible(1, 10, 20) ➞ 0
# # No number between 1 and 10 can be evenly divided by 20.

# evenly_divisible(1, 10, 2) ➞ 30
# # 2 + 4 + 6 + 8 + 10 = 30

# evenly_divisible(1, 10, 3) ➞ 18
# # 3 + 6 + 9 = 18
# Ans:

def check_func(a,b,c):
  x = 0
  for i in range(a , b + 1):
    if c == 0 :
      return 'can not devide value by 0'
    elif c > b :
      return f'can not evenly divided by number of {c} from range {a} to {b}'
    if i % c == 0:
      x = x + i

  return x

print(check_func(1,10,2))



# Question2. Create a function that returns True if a given inequality expression is correct and False otherwise.
# Examples
# correct_signs("3 < 7 < 11") ➞ True

# correct_signs("13 > 44 > 33 > 1") ➞ False

# correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
# Ans:

def check(s):
    regex=eval(s)
    if regex:
        return True
    else:
        return False 

print(check("2 < 7 < 15"))


# Question3. Create a function that replaces all the vowels in a string with a specified character.
# Examples
# replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

# replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

# replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
# Ans:

def replaceVowels(test_str, data):

    vowels = 'AEIOUaeiou'
 
    for ele in vowels:
        test_str = test_str.replace(ele, data)
    return test_str

print(replaceVowels('Himanshu','?'))


# Question4. Write a function that calculates the factorial of a number recursively.
# Examples
# factorial(5) ➞ 120

# factorial(3) ➞ 6

# factorial(1) ➞ 1

# factorial(0) ➞ 1
# Ans:

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print(recur_factorial(5))


# Question 5
# Hamming distance is the number of characters that differ between two strings.
# To illustrate:
# String1: "abcbba"
# String2: "abcbda"

# Hamming Distance: 1 - "b" vs. "d" is the only difference.
# Create a function that computes the hamming distance between two strings.
# Examples
# hamming_distance("abcde", "bcdef") ➞ 5

# hamming_distance("abcde", "abcde") ➞ 0

# hamming_distance("strong", "strung") ➞ 1

# Ans:

def hamming_distance(str1, str2):
    i = 0
    count = 0
 
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count
  
str1 = "abcde"
str2 = "bcdef"
 
print(hamming_distance(str1, str2))
