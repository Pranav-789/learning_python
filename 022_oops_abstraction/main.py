from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(abstract): #will throw error on call because no area and perimeter initialized according to python
    def __init__(self, side):
        self.side = side

class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print("I have created cirlc perimeter")
    
    def area(self):
        pass

obj = Circle(15)

#abstraction is not present by default in python, we achieve it through a library