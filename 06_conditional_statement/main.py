print("*****IF ELSE*****")

a = 9

# if a > 10:
#     print("a is greater than 10") #indentation should be followed, this indentation is making code go into if block
# else:
#     print("a is less than 10")

# money = int(input("please provide me money: "))

# if money == 10:
#     print("I will have a choco bar icecream")
# elif money == 20:
#     print("I will have a cone")
# elif money == 30:
#     print("I will have a frosty")
# else:
#     print("I will have a mango dolly")

# the flow goes as if -> elif -> else only one will be executed

#Q1
# num1 = input("Please enter first number: ")
# num2 = input("Please enter second number: ")

# if(num1 > num2):
#     print(f"{num1} is greater than {num2}")
# elif num1 == num2:
#     print(f"{num1} is equal to {num2}")
# else:
#     print(f"{num1} is less than {num2}")


#Q2
# gender = input("Please enter the gender(M/F): ")

# if(gender == "M"):
#     print("Good Morning Sir")
# elif(gender == "F"):
#     print("Good morning ma'am")
# else:
#     print("Invalid input")

#Q3
# number = int(input("Please enter a number: "))

# if number%2==0:
#     print(f"The number {number} is even")
# else:
#     print(f"The number {number} is odd")

#Q4
# Name = input("Please enter your name: ")
# Age = int(input("Please enter your age: "))

# if Age >= 18:
#     print(f'Hello {Name}, You are eligible for voting')
# else:
#     print(f"Sorry {Name}, You are not eligible for voting")


#Q5
# year = int(input("Enter the year: "))

# if year%100==0 and year%400==0:
#     print(f"The year {year} is a leap year")
# elif year%100 != 0 and year%4==0:
#     print(f"This year {year} is a leap year")

# else:
#     print("Not a leap year")

#Q6
temp = int(input("Enter the temperature: "))

if temp < 0:
    print("Freezing Cold!")
elif temp >= 0 and temp < 10:
    print("Very Cold!")
elif temp >= 10 and temp < 20:
    print("Cold")
elif temp >= 20 and temp < 30:
    print("Pleasant")
elif temp >= 30 and temp < 40:
    print("Hot")
else:
    print("Very Hot")
