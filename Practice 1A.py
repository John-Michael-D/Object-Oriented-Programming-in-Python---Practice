#object = A "bundle" of related attributes (variables) and methods (functions)
#Ex: phone, cup, book

#Ex of phone attributes:
#version_num = 13
#is_on = True
#Ex of cup attributes:
#liquid = "coffee"
#temp = 93.3
#is_empty = False
#Ex of book attributes:
#title = "The Hobbit"
#pages = 310

#Methods are functions contained within an object that cause the object to perform actions.
#Ex of phone methods:
#def make_call():
#def receive_call():
#def turn_on():
#def turn_off():
#Ex of cup methods:
#def fill_cup():
#def drink_cup():
#def empty_cup():
#Ex of book methods:
#def open_book():
#def read_book():
#def close_book():

#You need a "class" to create many objects.
#class = Blueprint used to design the structure and layout of an object.

from Practice1B import Car

car1 = Car("Honda Civic", 2024, "White", False)
print(car1.model) #The . in these statements is known as the attribute access operator.
print(car1.year)
print(car1.color)
print(car1.for_sale)

car2 = Car("Corvette", 2025, "Blue", True)
print(f"\n{car2.model}")
print(car2.year)
print(car2.color)
print(car2.for_sale)

print("\n")
car1.drive()
car1.stop()
car2.drive()
car2.stop()

print("\n")
car1.describe()
car2.describe()