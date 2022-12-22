1.	Set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt.
Ans:

Test1 =  'This is a test of the emergency text system'
f= open("test1.txt","w+")
f.write(Test1)
f.close()

2.	Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?
Ans: 
f=open("guru99.txt", "r")
tesr2 = f.read()
f.close()
print(tes2)
Its same

3. Create a CSV file called books.csv by using these lines:
title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
Ans:

4.	Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).
Ans:

import sqlite3
conn = sqlite3.connect('books.db')
c = conn.cursor()

c.execute('create table books(title varchar(20),author varchar(20), year int)')
conn.commit()

5.	Read books.csv and insert its data into the book table.
Ans:

from csv import writer

List = ['Small Gods','Terry Pratchett',1992]
 
with open('event.csv', 'a') as f_object:
 
    writer_object = writer(f_object)
 
    writer_object.writerow(List)
 
    f_object.close()


6.	Select and print the title column from the book table in alphabetical order.
Ans:

c.execute('select title from books order by title asc')
print(c.fetchall())

7. From the book table, select and print all columns in the order of publication.
Ans:
import csv
 
filename = open('book.csv', 'r')
 
file = csv.DictReader(filename)
 
title = []

author = []

year = []


header = ['title', 'author', 'year']



for col in file:
    title.append(col['title'])
    author.append(col[‘author’])
    year.append(col[‘year’])
 
print('title:', title)
print(‘author’,author)
print(‘year’,year)

8.	Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 6.
Ans:
import sqlalchemy
engine = sqlalchemy.create_engine("sqlite:///books.db")

9.	Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.
Ans:

import redis
conn = redis.Redis()
conn.delete('test')
conn.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})
conn.hgetall('test')

10.	Increment the count field of test and print it.
Ans:
conn.hincrby('test','count', 3)

