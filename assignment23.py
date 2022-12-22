


1. What is the result of the code, and why?
>>> def func(a, b=6, c=8):
print(a, b, c)
>>> func(1, 2)

Ans. This funtion is taking a positional argument and 2 keyward argument. When function call m=is made, parameter passed 
are a=1,b=2. When the function is executed , parameter c=8 will be taken by default as its a keyword argument.

1,2,8

2. What is the result of this code, and why?
>>> def func(a, b, c=5):
print(a, b, c)
>>> func(1, c=3, b=2)
Ans.
Ans. When we make function call, order will be positional argument and then keywords arguments. we can pass the keyword arguments in any order we want.

1,2,3

3. How about this code: what is its result, and why?
>>> def func(a, *pargs):
print(a, pargs)
>>> func(1, 2, 3)

Ans.The return type of *args parameter is tuple, where as **kargs will be dictionary

1,(2,3)

4. What does this code print, and why?
>>> def func(a, **kargs):
print(a, kargs)
>>> func(a=1, c=3, b=2)

Ans. The return type of  **kargs is  dictionary

1,{'c':3,'b':2}

5. What gets printed by this, and explain?
>>> def func(a, b, c=8, d=5): print(a, b, c, d)
>>> func(1, *(5, 6))

Ans. In the example the value *(5,6) will be unpacked and will be assigned to b and c and passed 
as arguments, d =5 will taken by defaults are keyword arguments.

1 5 6 5

6. what is the result of this, and explain?
>>> def func(a, b, c): a = 2; b[0] = 'x'; c['a'] = 'y'
>>> l=1; m=[1]; n={'a':0}
>>> func(l, m, n)
>>> l, m, n

Ans:

Its work on position arguments. here l = 1, m=[1],n={'a':0} . and pass it as arguments in the func. Inside the func that l,m,n values going 
to the a,b,c. There l change to 2,m changes to x and n changes to {'a':'y'}.

2 [x] {'a':'x'}



