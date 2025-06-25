# def show():
#     print("how are you?")
# def show(): #this overwrite the above written function
#     print("how are you bro?")

# show()

# class Animal:
#     def show(self):
#         print("Hello I am an Animal")

#     # def show(self, name): method overloading doesnt exist in python but overwriting does
#     #     self.name = name

# class Human(Animal):
#     def show(self):
#         print("Hey! I am a human.")

# obj = Human()
# obj.show()


#Duck Typing
class Animal:
    def show(self):
        print("I am showing")

class Human:
    def show(self):
        print("hello I am also showing")

obj = Animal()
obj2 = Human()

obj.show()
obj2.show()
