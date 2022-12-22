1.	Add the current date to the text file today.txt as a string.
Ans:
import datetime
from datetime import date
now = date.today()
cur_date = now.isoformat()
with open('today.txt','w') as file:
    file.write(cur_date)
     
2.	Read the text file today.txt into the string today_string
Ans:
with open('today.txt','r') as file:
    today_string = file.read()

3.	Parse the date from today_string.
Ans:
from datetime import datetime
format = '%Y-%m-%d'
datetime.strptime(today_string,format)

4.	List the files in your current directory
Ans:

import os
os.listdir('.')

5.	Create a list of all of the files in your parent directory (minimum five files should be available).
Ans:
import os
os.listdir('.')


6.	Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.
Ans:
import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print('sleeping 1 Second.....')
    x = range(1, 5)
    time.sleep(x)
    print('Done Sleeping....')

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)
p3 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')

7.	Create a date object of your day of birth.
Ans:
import datetime
from datetime import date

my_dob = date(1998,9,9)

8.	What day of the week was your day of birth?
Ans:
my_dob.weekday()

9.	When will you be (or when were you) 10,000 days old?
Ans:
from datetime import timedelta
day = my_dob + timedelta(days=10000)
     

