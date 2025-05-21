#Create a "Person" class
#Create an attribute "name" in the "Person" class
class Person:
    name="Jaloliddin"
    def __init__(self,year,work,name=None):
        self.year=year
        self.work=work
        if name:
            self.name=name
    def wid(self):
        print(f"{self.name} is {self.year} years old")
p1=Person(2003,"IT")
