import math
import random
my_num = 66
pow(2, 2) #Takes first number to the power of second
abs(-10) #Gets absolute value
round(3.141592) #Rounds
lst = [1,2,3,4,5]
results = map(simple, lst)
print(list(results))
math.factorial(42)
42.5.ceil()
math.sqrt(4)
math.sqrt(2)

#Looks at all contents list

print(random.choices("a","b","c", k=5 )) #chooses random

print(f"This is my num {my_num}")

HelloWorld = "Hello World"
HelloWorld.Capatalize()
HelloWorld.find("o") #finds first instance of characters in string
HelloWorld.isalnum() #if it's alpha numerical

#islower(), isspace(), istitle(), isupper(), isdigit
HelloWorld.endswith("d") #True or false

HelloWorld.isdigit(x)#gets digit

lst = [1, 2, 3, 4]

bst = [4,5,6]
lst.extend(bst)#adds bst to lst
lst.pop(0) #remofes item at given index
lst.sort() #sorts list