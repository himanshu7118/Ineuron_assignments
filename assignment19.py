1.	Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?
Ans: 
class Thing():
  pass

print(Thing())

<__main__.Thing object at 0x7fc18286a160>

example = Thing()

print(example)

<__main__.Thing object at 0x7fc18286aca0>

Its not same.


2.	Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters should be printed.
Ans:
class Thing2:
  letters = 'abc'
  print(letters)

Thing2()

3.	Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?
Ans:
class Things3():

  def __init__(self,letters):
    self.letters = letters

    print(self.letters)

Things3('xyz')

No

4.	Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values 'Hydrogen,' 'H,' and 1.
Ans:

class Element():

  def __init__(self,name,symbol,number):
    self.name = name
    self.symbol = symbol
    self.number = number

x = Element('Hydrogen','H',1)

print(x)

print(x.name)

print(x.symbol)

print(x.number)




5.	Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.
Ans:
dic = {
    'name': 'Hydrogen', 
    'symbol': 'H', 
    'number': 1
}

class Element():

  def __init__(self,name,symbol,number):
    self.name = name
    self.symbol = symbol
    self.number = number

x = Element(dic['name'],dic['symbol'],dic['number'])

print(x.name)

print(x.symbol)

print(x.number)

6.	For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.
Ans:
dic = {
    'name': 'Hydrogen', 
    'symbol': 'H', 
    'number': 1
}

class Element():

  def __init__(self,name,symbol,number):
    self.name = name
    self.symbol = symbol
    self.number = number

  def dump(self):
    return self.name,self.symbol,self.number

x = Element(dic['name'],dic['symbol'],dic['number'])

hydrogen = x.dump()

print(hydrogen)

7.	Call print(hydrogen). In the definition of Element, change the name of method dump to __str__, create a new hydrogen object, and call print(hydrogen) again.
Ans:
dic = {
    'name': 'Hydrogen', 
    'symbol': 'H', 
    'number': 1
}

class Element():

  def __init__(self,name,symbol,number):
    self.name = name
    self.symbol = symbol
    self.number = number

  def __str__(self):
     return "name:" + self.name +"\n" + "symbol:" + self.symbol +"\n"+ "number:" + str(self.number)

hydrogen = Element(dic['name'],dic['symbol'],dic['number'])

print(hydrogen)


8.	Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.
Ans:
dic = {
    'name': 'Hydrogen', 
    'symbol': 'H', 
    'number': 1
}

class Element():

  def __init__(self,name,symbol,number):
    self.__name = name
    self.__symbol = symbol
    self.__number = number

  def __str__(self):
     return "name:" + self.__name +"\n" + "symbol:" + self.__symbol +"\n"+ "number:" + str(self.__number)

hydrogen = Element(dic['name'],dic['symbol'],dic['number'])

print(hydrogen)

9.	Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.
Ans:
class Bear():

  def eats():
    return 'berries'

class Rabbit():

  def eats():
    return 'clover'

class Octothorpe():

  def eats():
    return 'campers'

bear = Bear.eats()

print(bear)

rabit = Rabbit.eats()

print(rabit)

octo = Octothorpe.eats()

print(octo)


10.	Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.
Ans:
class Laser():

  def does():
    return 'disintegrate'

class Claw():

  def does():
    return 'crush'

class SmartPhone():

  def does():
    return 'ring'

class Robot():

  def does(laser,claw,smartphone):
    print(laser,claw,smartphone)

laser = Laser.does()

rabit = Claw.does()

smart = SmartPhone.does()

robot = Robot.does(laser,rabit,smart)

print(robot)


