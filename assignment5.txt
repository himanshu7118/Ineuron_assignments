1.	What does an empty dictionary's code look like?
Ans: {}

2.	What is the value of a dictionary value with the key 'foo' and the value 42?
Ans: {‘foo’:42}

3.	What is the most significant distinction between a dictionary and a list?
Ans:  List is the collection of various index value pair.
Dictionary is collection of key , value pairs.

4.	What happens if you try to access spam['foo'] if spam is {'bar': 100}?
Ans: its showing a key error.

5.	If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
Ans: There is no difference. The in operator checks whether a value exists as a key in the dictionary. 'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam. values() checks whether there is a value 'cat' for one of the keys in spam .

6.	If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
Ans: There is no difference. The in operator checks whether a value exists as a key in the dictionary. 'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam. values() checks whether there is a value 'cat' for one of the keys in spam .

7. What is a shortcut for the following code?
if 'color' not in spam:
spam['color'] = 'black'
Ans: if spam.get('color') == None:
    spam['color'] = 'black'

8.	How do you "pretty print" dictionary values using which module and function?
Ans:
test_dict = {'gfg' : {'rate' : 5, 'remark' : 'good'}, 'cs' : {'rate' : 3}}
  
print("The original dictionary is : " +  str(test_dict))

for sub in test_dict:
    print (sub)
    for sub_nest in test_dict[sub]:
        print (sub_nest, ':', test_dict[sub][sub_nest])
