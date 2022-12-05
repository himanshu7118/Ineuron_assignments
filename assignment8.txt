1.	Is the Python Standard Library included with PyInputPlus?
Ans: PyInputPlus is not a part of the Python Standard Library, we must install it separately using Pip.

2.	Why is PyInputPlus commonly imported with import pyinputplus as pypi?
Ans:  so that you can enter a shorter name when calling the module's functions.


3.	How do you distinguish between inputInt() and inputFloat()?
Ans: inputInt() : Accepts an integer value. This also takes additional parameters 'min', 'max', 'greaterThan' and 'lessThan' for bounds. Returns an int. inputFloat() : Accepts a floating-point numeric value.


4.	Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
Ans: pyip. inputint(min=1, max=100) 


5.	What is transferred to the keyword arguments allowRegexes and blockRegexes?
Ans: keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input.

6.	If a blank input is entered three times, what does inputStr(limit=3) do?
Ans:  The function will raise RetryLimitException.

7.	If blank input is entered three times, what does inputStr(limit=3, default='hello') do?
Ans:  The function returns the value 'hello'.
