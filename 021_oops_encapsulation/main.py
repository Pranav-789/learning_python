class Factory:
    
    _a = "pune" #python doesnt have inbuilt protected, it is a naming convention\

    __c = 13 #this is a private attribute supported in python, cant be accessed outside the class

    def __show(self):
        print("hello i am a pune factory")

    #to access privates, we use something like getter, setter


class Bhopal(Factory):
    def show(self):
        print(super()._a)

Bhopal().show()
