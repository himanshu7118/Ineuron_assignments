# Question1
# Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
# Examples
# equal(3, 4, 3) ➞ 2

# equal(1, 1, 1) ➞ 3

# equal(3, 4, 1) ➞ 0 
# Notes
# Your function must return 0, 2 or 3.
# Ans:

def equal(a,b,c):
    num = 0
    if a == b and a == c :
        num = 3
    elif a == b or a == c :
        num = 2
    else:
        num = 0
    return num

print(equal(3, 4, 3))

# Question2
# Write a function that converts a dictionary into a list of keys-values tuples.
# Examples
# dict_to_list({
#   "D": 1,
#   "B": 2,
#   "C": 3
# }) ➞ [("B", 2), ("C", 3), ("D", 1)]

# dict_to_list({
#   "likes": 2,
#   "dislikes": 3,
#   "followers": 10
# }) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
# Notes
# Return the elements in the list in alphabetical order.
# Ans:

def dict_to_list(dict1):
  for i,j in dict1.items():
    yield (i,j)

d1 = dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
)}

var1 = list(d1)

print(var1)

# or 

def dict_to_list(dict1):
  return list(dict1.items())

print(dict_to_list({"likes": 2,"dislikes": 3,"followers": 10}))

# Question3
# Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
# Examples
# mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }

# mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }

# mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
# Notes
# All of the letters in the input list will always be lowercase.
# Ans:

def mapping(list1):
  return {i.lower():i.upper() for i in list1}

print(mapping(["p", "s"]))

# Question4
# Write a function, that replaces all vowels in a string with a specified vowel.
# Examples
# vow_replace("apples and bananas", "u") ➞ "upplus und bununus"

# vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"

# vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"
# Notes
# All words will be lowercase. Y is not considered a vowel.
# Ans:

def vow_replace(str1,rp):
    vowel ='AEIOUaeiuo'
    s1 = []
    for i in range(len(str1)):
        if str1[i] in vowel:
            s1.append(rp)
        else:
            s1.append(str1[i])

    return ''.join((s1))

print(vow_replace("apples and bananas", "u"))

# Question5
# Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.
# Examples
# ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"

# ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"

# ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."

def ascii_capitalize(s):
    s1 = []
    for i in range(len(s)):
        if ord(s[i]) % 2 == 0:
            s1.append(s[i].upper())
        else:
            s1.append(s[i].lower())

    return "".join((s1))

print(ascii_capitalize("to be or not to be!"))
