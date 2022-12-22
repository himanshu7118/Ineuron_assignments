1.How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60).
sol. 60 
Ans: 60 * 60 
2. Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.
Ans: seconds_per_hour  = 3600 * 60
3. How many seconds do you think there are in a day? Make use of the variables seconds per hour and minutes per hour.
Ans: 3600  *  60   *  24

4. Calculate seconds per day again, but this time save the result in a variable called seconds_per_day
Ans: seconds_per_day = seconds_per_hour  *  24

5. Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.
Ans: seconds_per_hour = seconds_per_day / seconds_per_hour  

6. Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree with the floating-point value from the previous question, aside from the final .0?
Ans:  Yes
seconds_per_day // seconds_per_hour  

7. Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
Ans: 
def gen_primes():
    n = 2
    primes = set()
    while True:
        for p in primes:
          if n % p == 0:
              break
          else:
              primes.add(n)
              yield n
          
          n += 1




