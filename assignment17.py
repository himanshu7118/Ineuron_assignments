1.	Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.
Ans: 
guess_me = 7
if guess_me >7:
  print('greater then 7')
elif guess_me <7:
  print('less then 7')
else:
  print('its 7')

2.	Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while loop that compares start with guess_me. Print too low if start is less than guess me. If start equals guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of the loop.
Ans: 
guess_me =7
start = 1

while start <= guess_me:
  print('its low')
  if start == guess_me:
    print('found it')
  start += 1
else:
  print('oops its greater then guess_me')

3.	Print the following values of the list [3, 2, 1, 0] using a for loop.
Ans: 
list1 = [3, 2, 1, 0]

for i in list1:
  print(i)

4.	Use a list comprehension to make a list of the even numbers in range(10)
Ans: 
ans = [ i for i in range(10) if i%2 ==0 ]
print(ans)

5.	Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the square of each key as its value.
Ans: 
ans = {i:i**2 for i in range(10)}
print(ans)


6.	Construct the set odd from the odd numbers in the range using a set comprehension (10).
Ans: 
new_set = {i for i in range(10) if i%2 != 0}

print(new_set)

7.	Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). Iterate through this by using a for loop.

Ans:   def gen_func(n):
  for i in range(n):
    yield ('got',i)

for i in gen_func(10):
  print(i)



8.	Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].
Ans: 
def good():
  return ['Harry', 'Ron', 'Hermione']


9.	Define a generator function called get_odds that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.
Ans: 
def get_odds():
  for i in range(10):
    if i%2 != 0:
      yield i

x = 0

for i in get_odds():
  x += 1
  if x == 3:
    print(i)

10.	Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch this exception and print 'Caught an oops'.
Ans:
class OopsException(Exception):
    pass

try:
    raise OopsException
except OopsException as e:
    print("Caught an oops")


11.	Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].
Ans: 

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
dictionary = dict(zip(titles, plots))
print(dictionary)


