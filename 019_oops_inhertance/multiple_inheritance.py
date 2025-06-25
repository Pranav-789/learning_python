class Animal:
    name1 = "lion"
    def __init__(self, name):
        pass

class Human:
    name2 = "Pranav"

    def __init__(self, name, age):
        pass

class Robots(Animal, Human): #whichever is written first will be targetted first
    #multiple inhertance
    name3 = "Charlie123"

obj = Robots("Tiger")

print(obj.name1)
print(obj.name2)
print(obj.name3)
