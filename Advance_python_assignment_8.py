Q1. What are the two latest user defined exception constraints in Python 3.X?
Ans: ArithmeticError, AttributeError , ImportError, IOError, FileNotFoundError, etc.

Q2. How are class based exceptions that have been raised matched to handlers?
Ans: When an exception is raised in Python, the interpreter looks for an exception handler that can handle the exception. Exception handlers are defined using a try-except block.
If an exception is raised within a try block, the interpreter looks for an except block that matches the type of the exception. This matching process is done by 
comparing the exception type to the types specified in the except blocks in the order they appear.

Q3. Describe two methods for attaching context information to exception artefacts.
Ans: 
Exception artifacts can be valuable sources of information for diagnosing and resolving software errors. To provide additional context to these artifacts, here are two methods for 
attaching context information:

1) Exception Logging: One approach is to log contextual information related to the exception when it is thrown. This can include details such as the time of the exception, the method or
 function where the exception occurred, the parameters passed to that method, the current state of the system, and any relevant metadata. These logs can then be reviewed and analyzed later 
 to gain a better understanding of the cause of the exception and the circumstances surrounding it.

For example, suppose an application throws an exception related to a user's failed login attempt. In this case, the logging mechanism could capture the user's login credentials, the time of 
the attempt, the user's IP address, and any other relevant information that could help diagnose the problem.

2) Custom Exception Types: Another approach is to create custom exception types that contain additional context information relevant to the specific error. This approach is 
useful when the context information is specific to the exception type, and not applicable to all exceptions that may occur in the system.

For example, suppose an application has a file processing component that throws exceptions related to file access errors. In this case, a custom exception type could be created 
that contains information such as the file name, the file path, and the operation that was being performed when the error occurred. This information can then be used to provide more targeted and informative error messages to the user, or to perform more detailed analysis of the error.

Q4. Describe two methods for specifying the text of an exception object's error message.
Ans: 
In Python, there are two methods for specifying the text of an exception object's error message:

Using the constructor of the exception class:
The most common way to specify the error message of an exception object is by passing the message string as an argument to the constructor of the exception class. For example, if you want to raise an exception with the error message "Invalid input", you can use the following code:
python
Copy code
raise Exception("Invalid input")
You can replace the "Exception" class with any other exception class that inherits from the base "Exception" class, such as "ValueError", "TypeError", or "AssertionError".

Setting the message attribute of the exception object:
Another way to specify the error message of an exception object is by setting the "message" attribute of the exception object. For example:
python
Copy code
try:
    # some code that might raise an exception
except Exception as e:
    e.message = "Invalid input"
    raise e

In this case, we catch the exception object and then set its "message" attribute to the desired error message before re-raising the exception. Note that not all exception classes have a "message" attribute, so this method might not work for all types of exceptions.

Q5. Why do you no longer use string-based exceptions?
Ans: String-based exceptions were used in older versions of Python, but they have been deprecated since Python 2.6 and are no longer used in modern versions of Python. The primary reason for this is that string-based exceptions lack important features and are less flexible than class-based exceptions. Here are some reasons why string-based exceptions are no longer used in Python:

Lack of structure and functionality:
String-based exceptions do not provide any structure or functionality beyond the error message itself. This makes it difficult to handle different types of exceptions differently or to provide additional information about the exception.

Difficult to catch and handle:
String-based exceptions can be difficult to catch and handle because they are not unique objects. If two different parts of the code raise exceptions with the same error message, it is difficult to determine which exception was raised.

Harder to extend or customize:
Class-based exceptions in Python are easy to extend or customize by inheriting from the base exception class and adding additional functionality. String-based exceptions, on the other hand, do not provide an easy way to extend or customize them.

Inconsistent with Python's object-oriented design:
Python is an object-oriented language, and class-09based exceptions are consistent with its object-oriented design. String-based exceptions do not fit well with Python's object-oriented approach.


