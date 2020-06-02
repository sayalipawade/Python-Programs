#If you want to access and change the private variables, accessor (getter) methods 
#and mutators(setter methods) should be used, as they are part of Class. 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
 
    def display(self):
        print(self.name)
        print(self.__age)

    def setAge(self, age):
        self.__age = age
 
    def getAge(self):
        print(self.__age)
 
#Creating object of class 
person = Person('sayali', 23)

#accessing using class method
person.display()

#changing age using setter
person.setAge(24)
person.getAge()