print("*****ARITHMETIC OPERATOR*****")
a=12
b=20

print("a+b = ", a+b)
print("b-a = ", b-a)
print("a*b = ", b*a)
print("b/a = ", b/a) #will return a float always
print("b//a = ", b//a) #Floor divison return the int value floored for rounding
print("5**3 = ", 5**3) #power/exponential
print("32%5 = ", 32%5) #remainder on division

#Python follows BODMAS rule for operation

#assignment operator
print("*****Assignment operators*****")
k = 23  # '=' is a assignment operator

#compound assignment operations

l = 20

l += 20 # l = l + 20
print("l = ",l)

l += 40
print("l = ",l)

l += 60
print("l = ",l)

l -= 10
print("l = ",l)

l *= 2
print("l = ",l)

l /= 2
print("l = ",l)

l //= 2
print("l = ",l)

print("*****Comparision operators*****")

a = 12.1
b = 12

print("a == b: ", a==b) #equals comparison
print("a != b: ", a!=b) #not equals comparison

print("a > b: ", a > b)
print("a < b: ", a < b)
print("23 > 23: ", 23 > 23)
print("23 >= 23: ", 23 >= 23)

print("*****STRING COMPARISON*****")
print(ord("A")) #65
print(ord("B")) #66
print("A" > "B")

print("ABC > ABB","ABC" > "ABB")
print("ABC > ACD","ABC" > "ACD")

# print("A" > 34) #ERROR as string can be compared only with string

print("*****LOGICAL OPERATOR*****")
#used for combining comparison
#Three logical operators: and, not, or

print("AND OPERATOR: Two logics combined: 123 > 100, 34 ==34: ", 123 > 100 and 34==34)

print("OR OPERATOR: If even one logic is true: ", 12 != 12 or 23 == 45 or 10 > 5)

print("NOT OPERATOR: reverses the boolean value: ", not 12 == 12)

print(True and bool(0))