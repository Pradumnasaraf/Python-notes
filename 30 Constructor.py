class Point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

point1 = Point(10,2)
print(point1.x)
        
#example

class Person:
    name=""
    def __init__(self, name) :
        self.name = name
        
    def talk(self):
        print(f'Hi, I am {self.name}') 

john = Person("Hello")
john.talk()

bob = Person("Rayan")
bob.talk()