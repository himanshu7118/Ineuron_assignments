1.What are the two values of the Boolean data type? How do you write them?
Ans: two values of Boolean data type:
0 = False
1= True


2. What are the three different types of Boolean operators?
Ans:  and, or , and not


3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
Ans: 
A	B	A and B      A or B          A and not B
True	True	True            True               False      
False	True	False           True               True
True	False	False           True               True
False	False	False            False             True
List = [(True,True),(False,True),(True,False),(False,False)]

4. What are the values of the following expressions?
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
Ans: (5 > 4) and (3 == 5) = False
not (5 > 4) = False
(5 > 4) or (3 == 5) = True
not ((5 > 4) or (3 == 5)) = False
(True and True) and (True == False) = False
(not False) or (not True) = True

5. What are the six comparison operators?
Ans:  >, <,>=,<=, ==, !=

6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
Ans:
Here ‘=’ is use to assign any value to the variable.
And ‘==’ is use to compare the value of both left and right side.
Ex : assignment operator
X = 5
Ex: 
X == 5
Here it check the X value is 5 or not.

7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')
Ans: 
ham
spam
spam
if spam = 11 
ans is : bacon
if spam = 10
ans is: 
eggs
bacon
if spam = 1 or 2 or 3 or 4
ans is :
ham
spam
spam

8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
Ans: spam = 1
spam = 1
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')


9.If your programme is stuck in an endless loop, what keys you’ll press?
Ans: ctrl + c

10. How can you tell the difference between break and continue?
Ans: break can break the loop if contidion match and continue will continue the loop from the starting when the condition match.

11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Ans:  ans is remain same in every condition of for loop.
for i in range(10):
      print(i)
ans: 0
1
2
3
4
5
6
7
8
9 
Here in for loop range(0,10) is start with 0 and go the 10-1 
for i range(0,10):
     print(i)
ans: 0
1
2
3
4
5
6
7
8
9
Here in for loop range(10) is start with 0 and go the 10-1
for i in range(0,10,1):
      print(i)
ans: 0
1
2
3
4
5
6
7
8
9
Here in for loop range(0,10,1) is start with 0 and go the 10-1 with a difference of 1 .

12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
Ans: 
for i in range(1,11):
  print(i)

i = 1
while i < 11:
  print(i)
  i += 1

13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
Ans:  spam.bacon()

