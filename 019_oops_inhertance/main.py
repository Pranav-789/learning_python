class Factory: #parent class/ super class
    a = "I am a attribute mentioned inside Factory"
    def hello(self):
        print("Hello , I am a method mentioned inside Factory")

class FactoryPune(Factory): #child class/subclass, inherited Factory class
    pass 

obj = FactoryPune()

print(obj.a)
print(obj.hello())

# I am a attribute mentioned inside Factory
# Hello , I am a method mentioned inside Factory
# None
# Because there are two print statements. First is inside function and second is outside function. When a function doesn't return anything, it implicitly returns None.


# Constructor in inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Hello, from {self.name}")


# class Human(Animal): #this has also innherited constructor from parent
#     pass

# person1 = Human("Pranav")
# person1.show()

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name) #targets parent class
        self.age = age
    
    def show(self): #same name, results in calling shild class fuction
        print(f"This is a object of {self.name}, and the age is {self.age}")

animal1 = Animal("lion")
person1 = Human("Pranav", 19)

person1.show()