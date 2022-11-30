1.	Why are functions advantageous to have in your programs?
Ans: Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update.

2.	When does the code in a function run: when it's specified or when it's called?
Ans: When it’s called

3.	What statement creates a function?
Ans: def

4.	What is the difference between a function and a function call?
Ans: A function is a block of code that does a particular operation and returns a result. It usually accepts inputs as parameters and returns a result. The parameters are not mandatory. A function call is the code used to pass control to a function.

5.	How many global scopes are there in a Python program? How many local scopes?
Ans: local scope means any statement or variable you define inside the function its call local scope statement or local scope variable.

When you define any statement or variable outside the function its call global scope variable or global scope statement.

6.	What happens to variables in a local scope when the function call returns?
Ans: After function call returns that local scope variable  will destroy.


7.	What is the concept of a return value? Is it possible to have a return value in an expression?
Ans: In return value you can return any value as per you want inside the func.
Its possible to return expression value.

8.	If a function does not have a return statement, what is the return value of a call to that function?
Ans: return None without that return func.

9.	How do you make a function variable refer to the global variable?
Ans: you can use the global keyword to declare which variables are global.

10.	What is the data type of None?
Ans: <class 'NoneType'>

11.	What does the sentence import are all your pets named eric do?
Ans: After import we can access func of that module.

12.	If you had a bacon() feature in a spam module, what would you call it after importing spam?
Ans: spam.bacon()

13.	What can you do to save a programme from crashing if it encounters an error?
Ans: with the help of try and except block.

14.	What is the purpose of the try clause? What is the purpose of the except clause?
Ans: If your func or any statement return error but you want to continue the logic or continue the for loop that time you use try except.

If your logic fail somewhere it directly go inside except block and return the error or default value which you set without stopping the execution.

