#Object oriented programming functional vs object oriented 
#Object is a thing like a list
#Create custom lists or custom clases
#Class naming convention
class Sample:
    pass
#insantiate
    x = Sample()
print(type(x))

class Dog:
    def __init__(self, breed): #gives it these attributes
        self.breed = breed#sets the attribute to the above attribute
sam = Dog(breed="Lab")#sets breed attirbute to dog
print(sam.breed)

#adding another attribute
class Dog:
    species = "mammal"
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
sam = Dog("Lab", "Sam") #(cant be redefined unless making a new class (which takes ram)) have to fill out all attributes with something

print(sam.species)
print(sam.name)
print(sam.breed)

class Circle:
    pi = 3.14
    def __init__(self, radius = 1):
        self.area = radius * radius * Circle.pi #create new attribute the sameway
        #reseting radius

def setRadius(self, newRadius): #creating methods, "things that do things"
    self.radius = newRadius #Change value of radius
    self.area = newRadius * newRadius * Circle.pi
#Polymorphism
#Special methods
#inheritance
class Animal:
    def __init__(self):
        print("Animal Criteria")
    def eating(self):
        print("Eating")
class Dog(Animal): #takes all atributes of this

    