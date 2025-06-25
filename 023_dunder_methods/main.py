#dunder methods are special methods which start and end with '__'
#automatically get called when you perform certain action on an object

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return ("hello, how are you?")
    
    def __add__(self, other): #not more object supported, you can you args and kargs
        sum = 0
        for i in other:
            sum = sum + i.age
        return (f"you sum of ages are {self.age +sum}")
    
    # def __add__(self, other): #not more object supported, you can you args and kargs
        # return (f"you sum of ages are {self.age +sum + other.age}")

obj = Animal("lion", 12)
obj2 = Animal("dolphin", 14)
obj3 = Animal("Tiger", 13)

print(obj) #if __str__ was not applied this would have given address of the object
#Now this access the __str__ 

# print(obj+obj2)
print(obj + (obj2, obj3)) #for now you can send it in tupple form, the third object