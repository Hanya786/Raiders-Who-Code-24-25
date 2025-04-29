'''
class inheritance in python
'''

'''
write a parent class and a child class of anything you like (but make it make sense). write it in 3 ways:
1. the child class inherits ALL properties and methods from the parent.
2. the child class inherits SOME properties from the parent.
3. the child class inherits NO properties from the parent.
4. the child class inherits properties from the parent AND has its own properties and methods.
5. create another parent class. have the child class inherit properties from both classes.
'''

class FParent():

  def __init__(self, fname, letter):
    self.fname = fname
    self.letter = letter

class LParent():

  def __init__(self, lname, number):
    self.lname = lname
    self.number = number

# 1
class Child1(FParent):
  pass


