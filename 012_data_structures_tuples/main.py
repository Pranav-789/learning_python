#Tuple data structures

#Syntax

a = (1, 2, 3, 4, 5.5, True)

print(type(a)) #class tuple


#PROPERTIES
#-> Immutable: cant modify values inside tuple
#->Duplicates: allowed
#->Ordered: index accessing allowed, like list and string
#->Heterogenous: different data structures allowed

#Traversing

# method 1
# for i in a:
#     print(i)

# method 2
# for i in range(len(a)):
#     print(a[i])

#methods in tuple
index = a.index(4)
print("4 is at index ", index)

count = a.count(1)
print("1 appeared ", count, " times.") #output will be 2 because True is also counted as 1

b, c, d, e = (1, 2, 3, 4) #unpacking tupple into respective variable

print("b ", b)
print("c ", c)
print("d ", d)
print("e ", e)

f = (1)

print(type(f)) #not tuple, just int, because you are passing only single value

g = (2, )
print(type(g)) #tuple, because here the tuple is not unpacked