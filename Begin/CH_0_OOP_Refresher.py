# Introduction to Object-Oriented Programming with Python: Creating and Using Classes

# Class Definition
class Car:

# Constructor (Initialization) - __init__ method
 def __init__(self,make,model):
# Encapsulation: Attributes (make and model) are encapsulated within the class.
  self.make = make
  self.model = model

# Method - start_engine
def start_engine(self):
    print(f"The {self.make} {self.model} ' s engine is running!")
# Encapsulation: Accessing attributes through self.


# Creating instances (objects) of the Car class

# Inheritance: Car is a class that can be used to create objects (instances).
  Car1 = Car("Toyota","Camery")
  Car2 = Car("Ford","Mustag")
# Abstraction: We create objects without worrying about the internal details of the Car class.
print(f"i have a {Car1.make} {Car1.model}")
print(f"i have a {Car2.make} {Car2.model}")
# Creating the first car (object)

# Creating the second car (object)


# Accessing object attributes

# Encapsulation: Accessing object attributes (make and model) using dot notation.


# Calling object methods

# Polymorphism: Different objects (car1 and car2) can perform the same action (start_engine).


# Method Call - start_engine
Car1.start_engine()
Car2.start.engine()