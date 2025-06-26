class Animal:
    @property
    def show(self):
        print("Hello, how are you? (Instance)")

obj = Animal()

# obj.show()
obj.show

#decorator is just a function that modify another function without changing it's actual code

def decorate(func): #passing function as an argument
    def wrapper():
        print("I will print myself before the function hello")
        func()
        print("I will print myself after the function hello")
    return wrapper


@decorate
def hello():
    print("Hello, I am Pranav")

hello()


def decorateADDER(func):
    def wrapper(a, b):
        print("The addition of given numbers is as follows!")
        func(a, b)
        print("Hope you like it")
    return wrapper

@decorateADDER
def addition(a, b):
    print(f"The sume of {a} and {b} is {a+b}")

addition(25, 56)
