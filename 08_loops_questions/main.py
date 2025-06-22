#Q1
# n = int(input("Please enter a number: "))

# for i in range(n): #default start = 0, end = n-1, steps = 1
#     print("Hello world")

#Q2
# n = int(input("Enter the number of natural numbers: "))

# for i in range(1, n+1): #steps by default 1
#     print(i)

#Q3 reverse for loop

# n = int(input("How many natural numbers to be printed: "))

# for i in range(n, 0, -1):
#     print(i)

#Q4 print table

# n = int(input("Enter the table number: "))

# for i in range(1, 11):
#     print(f"{n} X {i} = {n*i}")

#Q5
# sum = 0
# n = int(input("Enter the number: "))

# for i in range(1, n+1):
#     sum += i

# print(f"Sum of {n} natural numbers = {sum}")

#Q6
# factorial = 1
# n = int(input("Enter the number: "))

# for i in range(1, n+1, 1):
#     factorial*=i

# print(f"factorial of {n} = {factorial}")

#Q7
# evenSum = 0
# oddSum = 0

# n = int(input("Enter the range: "))

# for i in range(1, n+1, 1):
#     if i%2==0:
#         evenSum += i
#     else:
#         oddSum += i

# print(f"Sum of even number between 1 and {n} = {evenSum}")
# print(f"Sum of odd number between 1 and {n} = {oddSum}")

#Q8

# n = int(input("Enter the number: "))

# print(f"****factors of {n}****")

# for i in range(1, n+1, 1):
#     if n%i == 0:
#         print(f"{i} is a factor of {n}")

#Q9
# n = int(input("Enter the number: "))

# factorSum = 0

# for i in range(1, n+1, 1):
#     if(n%i == 0  and i != n):
#         factorSum += i

# if(factorSum == n):
#     print(n, " is a perfect number")
# else:
#     print(n, " is not a perfect number")

#Q10

# factorCount = 0
# n = int(input("Enter the number: "))

# for i in range(1, n+1, 1):
#     if n%i == 0:
#         factorCount+=1

# if factorCount == 2:
#     print(f"The number {n} is a prime number")
# else:
#     print(f"The number {n} is not a prime number")

#Q11
# stringName = "Pranav"
# reversedName = ""

# for i in range(len(stringName)-1, -1, -1):
#     reversedName = reversedName + stringName[i]

# print(reversedName)

#Q12
# stringName = input("Enter a string: ")
# reversedName = ""

# for i in range(len(stringName)-1, -1, -1):
#     reversedName = reversedName + stringName[i]

# if(stringName == reversedName):
#     print(f"{stringName} is a palindrome")
# else:
#     print(f"{stringName} is not a palindrome")

#Q13
a ="HHdjsfanr131478dafdja5&*&%^*@"

char = 0
digits = 0
spchr = 0

for i in a:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        char+=1
    else:
        spchr+=1

print(f"digits: {digits}\nAlphabets: {char}\nSpecial charcter: {spchr}")