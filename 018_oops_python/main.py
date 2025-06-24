class Car:
    brand = "Toyota" #attribute

    def startEngine(self): #method
        print("Toyota engine started")
    
    # print("The Car class is initialized") #this line will be executed when program runs initially only
    

# print(Car().brand)
# Car().startEngine()

obj = Car()

print(obj.brand)
obj.startEngine()


class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
    
    def show(self):
        print(f"Your object details are {self.material, self.zips, self.pockets}")


#creating an instance/object of the class Factory
rebook = Factory("leather", 3, 2) #self keyword tracks the location of the object, here rebook

campus = Factory("nylon", 3, 2)

print("Material used in campus: ", campus.material)
rebook.show() 


class Animal:
    name = "lion" #class attribute
    def __init__(self, age):
        self.age = age #instance attribbute, the ones dfined with self

    def show(self): #instance method, because of self
        print(f"The age is {self.age}")

    #for class method a decorator as following is required
    @classmethod
    def hello(cls): #cls tracks class, not object
        print("How are you Bro?") #it does not attributes assigned by self

    #static method, not tracks class or object

    @staticmethod
    def static():
        print("Static_ How are you?")

obj = Animal(12)

obj.static()