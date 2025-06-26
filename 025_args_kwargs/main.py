#keyword in python used in function definition to accept flexible number of arguments

print("\n\n******ARGS AND KWARGS******\n\n")
# def addition(*args): #now the incoming arguments are provided in a tuple form
#     sum = 0
#     for i in args:
#         sum += i
#     print("The sum of given numbers is: ", sum)

# addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def addition(**kwargs): #to capture keywords arguments
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

addition(a = 18, g = 43, h = 12, d = 13)


print("\n\n******ARGS AND KWARGS WITH DECORATORS******\n\n")

def decorateADDER(func):
    def wrapper(*args, **kwargs):
        print("The addition of given numbers is as follows!")
        func(*args, **kwargs)
        print("Hope you like it")
    return wrapper

@decorateADDER
def addition(a, b):
    print(f"The sume of {a} and {b} is {a+b}")

addition(25, 56)


print("\n\n******COMPREHENSION******\n\n")

# a = 12
# print("Even") if(a%2==0) else print("Odd")

# l = []

# for i in range(1, 21):
#     if(i % 2==0):
#         l.append(i)

# print(l)

#or you can write a list comprehension
l = [i for i in range(1, 21) if i % 2 == 0]
print(l)

#dictionary comprehension
dic = {i : i**2 for i in range(1, 10)}
print(dic)



#Lambda function
print("\n\n******LAMBDA FUNCTION******\n\n")

addition = lambda a, b : a+b
print(addition(12, 13))

isEven = lambda a: "even" if a%2==0 else "odd"
print(isEven(9))



print("\n\n******MAP FILTER ZIP******\n\n")

#map is used to apply function to multiple items
#takes a list or any sequence
#applies the function to every item of the sequence

a = [1, 2, 3, 4, 5]

result = map(lambda x : x*2, a)

def double(x):
    return x*2
result2 = map(double, a) #map accepts function and a iterable


print(result)
print(list(result))
print(list(result2))


def even(x):
    return (x %2 == 0)

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result3 = filter(even, list_a)

print(result3)
print(list(result3))
