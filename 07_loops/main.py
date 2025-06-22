count = 0

# while count < 10:
#     print(f"{count}. Hello world")
#     count += 1

#For loop
a = range(1, 11, 1) #end exclude one from end

# for i in a:
#     print(f"{i}. hello world")

# for i in range(1, 21, 1):
#     print(f"{i}. hello world")

# for i in range(21): #loop starts from 0 goes till 21 with steps as 1 at a time
#     print(i)

# for i in range(16, 0, -1): #reverse looping
#     print(i)

# for i in range(-5, -16, -1):
#     print(i)

# n = int(input("Enter the number for table: "))
# for i in range(1, 11, 1):
#     print(f"{n} x {i} = ", n*i)

#loops for string

#method 1
# string1 = "Pranav"

# for i in range(len(string1)): #length is already +1 as length is counted from 1, and string is inddexed from 0
#     print(string1[i])

#method 2
# for i in string1:
#     print(i)

# for i in range(1, 21):
#     if i == 15:
#         break #breaks the loop at i equals 15
#     else:
#         print(i)

# for i in range(1, 21):
#     if i == 15 or i == 10:
#         continue #skips the iteration at i equals 15
#     else:
#         print(i)

for i in range(1, 21):
    if i == 55:
        print("Break statement is executed")
        break
    print(i)
else:
    print("Break statement is not executed")