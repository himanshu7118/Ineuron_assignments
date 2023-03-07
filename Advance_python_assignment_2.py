Q1. What is the relationship between classes and modules?
Ans: Classes may generate instances (objects), and have per-instance state (instance variables). Modules may be mixed into classes and other modules. The mixed-in module's constants and methods blend into that class's own, augmenting the class's functionality. Classes, however, cannot be mixed into anything.


Q2. How do you make instances and classes?
Ans: To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts.



Q3. Where and how should be class attributes created?
Ans: 
1.	A class attribute is shared by all instances of the class. To define a class attribute, you place it outside of the __init__() method.
2.	Use class_name. ...
3.	Use class attributes for storing class contants, track data across all instances, and setting default values for all instances of the class.



Q4. Where and how are instance attributes created?
Ans : Instance attributes are defined in the constructor. Defined directly inside a class. Defined inside a constructor using the self parameter.



Q5. What does the term "self" in a Python class mean?
Ans:  The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.


Q6. How does a Python class handle operator overloading?
Ans: The operator overloading in Python means provide extended meaning beyond their predefined operational meaning. Such as, we use the "+" operator for adding two integers as well as joining two strings or merging two lists. We can achieve this as the "+" operator is overloaded by the "int" class and "str" class.



Q7. When do you consider allowing operator overloading of your classes?
Ans: When one or both operands are of a user-defined class or structure type, operator overloading makes it easier to specify a user-defined implementation for such operations. This makes user-defined types more similar to the basic primitive data types in terms of behavior.



Q8. What is the most popular form of operator overloading?
Ans: The most frequent instance is the adding up operator '+', where it can be used for the usual addition and also for combining two different strings.



Q9. What are the two most important concepts to grasp in order to comprehend Python OOP code?
Ans: Both inheritance and polymorphism are fundamental concepts of object oriented programming.
