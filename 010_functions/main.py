#Functions

#how to create a function
#Syntax below

def hello():
    print("hello user")

#this was how a function is created


#after creating, call the function to use
for i in range(0, 5, 1):
    hello()

#passing parameters function

def sum(a, b): #The thing you accept are parameters
    print("The sum of your numbers is: ", a+b)

sum(3, 4) #the thing you pass are called arguments
#This was an example off positional arguments

#Let's explore default arguments

def hello(name, age):
    print(f"Hello {name}, your age is {age}")

hello(age = 19, name = "pranav")#keyword arguments, no need for following position

def sumII (a= 0, b = 0):
    print(f"The sum of the numbers is {a + b}")

sumII(45) #Default argument b as 0


def isPalindrome(st):
    rev = ""
    for i in range(len(st)-1, -1, -1):
        rev = rev + st[i]
    
    if rev == st:
        print("Palindrom")
    else:
        print("not a palindrome")

isPalindrome("racecar")
isPalindrome("pranav")
#function is a reusable block of code

def helloII():
    return "hello how are you?"

helloString = helloII()
print(helloString)