1.	Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.
Ans:
# Example in zoo.py file:

def hours():
  print('Open 9-5 daily')

# In interpreter:

import zoo

zoo.hours()

2.	In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
Ans:

# Example in zoo.py file:

def hours():
  print('Open 9-5 daily')

# In interpreter:

import zoo as menagerie

print(menagerie.hours())


3.	Using the interpreter, explicitly import and call the hours() function from zoo.
Ans: 
import zoo
zoo.hours()


4.	Import the hours() function as info and call it.
Ans: import zoo.hours() as info
Info()

5.	Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.
Ans: 
plain = {
'a': 1,
 'b': 2, 
'c': 3
}

6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?
Ans: 
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

for key,value in od.items():
	print(key,value)

It is in different order

7.Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].
Ans:
dict_of_lists = {}
dict_of_lists['a'] = 'something for a'
print(dict_of_lists['a'])



