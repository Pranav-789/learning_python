#wrong syntax, wromg indentation, and tab error cant be handeled
#all other error are exception

a = int(input("Tell your number: "))

# print(10/a) #if a = 0, there will be ZeroDivisionError
#because of error flow will stop
#this thing is known as exceptions

try: #requires atleast one except or finally block
    print(10/a)
except Exception as err:
    print(f"sorry there is an error as {err}")
else:
    print("good there is no exception")
finally:
    print("i will run no matter what")

print("Ok i have done the divison")

print("\n")

age = int(input("tell you age: "))

try:
    if age < 10 or age > 18:
        raise ValueError("Your age must be between 10 and 18")
    else:
        print("welcome to to the club")
except Exception as err:
    print(f"An error occured as {err}")

print("The club will start soon")