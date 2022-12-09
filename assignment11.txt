1.	Create an assert statement that throws an AssertionError if the variable spam is a negative integer.
Ans: assert spam >= 0

2.	Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
Ans:  assert eggs.lower() != bacon.lower()

3.	Create an assert statement that throws an AssertionError every time.
Ans: assert()

4.	What are the two lines that must be present in your software in order to call logging.debug()?
Ans:
To be able to call logging.debug(), you must have these two lines at the start of your program:

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
%(levelname)s - %(message)s')

5.	What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
Ans: 
To be able to send logging messages to a file named programLog.txt with logging.debug(), you must have these two lines at the start of your program:

import logging
>>> logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
format=' %(asctime)s - %(levelname)s - %(message)s')

6.	What are the five levels of logging?
Ans:
DEBUG, INFO, WARNING, ERROR, and CRITICAL

7.	What line of code would you add to your software to disable all logging messages?
Ans: 
logging.disable(logging. DEBUG)

8.Why is using logging messages better than using print() to display the same message?
Ans: You can disable logging messages without removing the logging function calls. You can selectively disable lower-level logging messages. You can create logging messages. Logging messages provides a timestamp.

8.	What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
Ans: 
Step Into
A method is about to be invoked, and you want to debug into the code of that method, so the next step is to go into that method and continue debugging step-by-step.
Step Over
If the line does not contain a function it behaves the same as “step over” but if it does the debugger will enter the called function and continue line-by-line debugging there.
Step Out
Step out – An action to take in the debugger that returns to the line where the current function was called.

10.After you click Continue, when will the debugger stop ?
Ans: Continue execution, only stop when a breakpoint is encountered. Set the next line that will be executed. Only available in the bottom-most frame. This lets you jump back and execute code again, or jump forward to skip code that you don't want to run.

11. What is the concept of a breakpoint?
Ans To break the logic or program when the certain condition match.

