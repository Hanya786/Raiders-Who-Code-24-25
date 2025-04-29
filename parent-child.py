'''
class inheritance in python


create an Animal object and use its functions. then, create a Dog object and use its functions. then, use the functions from the Animal class on the Dog object.
'''
class Animal():

  def __init__(self, name, age, species):
    self.name = name
    self.age = age
    self.species = species

  def introduction(self):
    print(f"This animal is named {self.name} and is {self.age} years old. It is a {self.species}.")

  def age_up(self):
    self.age += 1

# take note of the way this is written --> Dog(Animal)
class Dog(Animal):

  def __init__(self, name, age, species, breed):
    super().__init__(name, age, species)
    self.breed = breed

  def explain_breed(self):
    print(f"This dog is a {self.breed}.")

  '''
  notice that the Dog object inherits the properties and methods from the Animal class? this is known as Python Inheritance.

  if our Dog class did not have an __init__ function, it would inherit the properties and methods from the Animal class and would not have a breed property or an explain_breed method.
  if the Dog class had an __init__ function and the __init__ function did not contain super(), it would NOT inherit the properties of the Animal class (the __init__ function overwrites them).

  write a parent class and a child class of anything you like (but make it make sense). write it in 3 ways:
  1. the child class inherits ALL properties and methods from the parent.
  2. the child class inherits SOME properties from the parent.
  3. the child class inherits NO properties from the parent.
  4. the child class inherits properties from the parent AND has its own properties and methods.
  5. create another parent class. have the child class inherit properties from both classes.
  '''

class YourClass():
  pass

