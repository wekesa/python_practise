"""
- Object oriented programming in python
- python supports multiple programming approaches
- One of the most popular one is by creating objects.
- An object has 2 characteristics
  - attributes
  - behaviour

- An example:
  - A parrot is can be an object as it has the following attributes:
    - name, age, color -> attributes
    - singing and dancing -> behavior
The concept of OOP is creating reusable code (DRY)

Principles of OOP
1. Class: It is a blueprint of an object. We can think of a class as a sketch of a parrot with labels.
   - class Parrot:
        pass
   - We construct instances from a class. An instance is a specific object created from a particular class.
2. Object: An object is an instantiation of a class. When a class is defined, only the description for the object is
   defined. Therefore, no memory or storage is allocated.
    - obj = Parrot()
3. Inheritance:
   - It is a way of creating a new class for using details of an existing class without modifying it. The newly formed
     class is a derived class. The existing class is a base class
4. Encapsulation: We restrict access to methods and variables in python by using underscore as prefix.
   - _ or __.
5. polymorphism is an ability  to use a common interface for multiple forms.
"""
class Computer:
    def __init__(self):
        self.__maxprice = 1000

    def sell(self):
        print("Selling price : {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price



class Bird:
    def __init__(self):
        print ("Bird is ready")

    def who_is_this(self):
        print("A Bird")

    def swim(self):
        print("Swimming is not my thing")

class Penguin(Bird):
    def __init__(self):
        super().__init__():
        print("Penguin is ready")

    def who_is_this(self):
        print("Penguin")

    def run(self):
        print("I run so fast")


# Creating a class and objects in Python
class Parrot:
    # class attribute
    species = "bird"

    # Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # methods which describe the behaviour
    def sing(self, song):
        return "{} sing this {} song".format(self.name, song)

blu = Parrot("Blu", 10)
red = Parrot("Red", 10)

# Access class attribute
print("Blu is a {}".format(blu.__class__.species))
print("Red is a {}".format(red.__class__.species))

# Access instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(red.name, blu.age))
