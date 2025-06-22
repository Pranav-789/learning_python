#Q basics
# n = 1

# while n <= 30:
#     print(n)
#     n+=1

#Q1 seperate digits
# n = 12343

# while n>0:
#     print(n%10)
#     n = n//10

#Q2
# n = int(input("Enter a number: "))

# newNumber = 0

# while n > 0:
#     newNumber = newNumber*10 + n%10
#     n = n//10

# print("Reversed number: ", newNumber)

#Q3
# n = int(input("Enter a number: "))

# oldNumber = n

# newNumber = 0

# while n > 0:
#     newNumber = newNumber*10 + n%10
#     n = n//10

# if(newNumber == oldNumber):
#     print(f"{oldNumber} is palindromic number")
# else:
#     print(f"{oldNumber} is not palindromic number")

#Q4 Mini game
import random 
#library in python for random generation

num = random.randint(1, 11)
while True:
    guessedNumber = int(input("Guess the number: "))
    if(num == guessedNumber):
        print("COngratualion you  guessed correct number ", num)
        break
    elif num < guessedNumber:
        print("guess lesser!")
    elif num > guessedNumber:
        print("guess higher!")