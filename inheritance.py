#Base
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Child class
class Student(Person):
    pass

#Object of person class 
x = Student("sayali", "pawade")
x.printname() 