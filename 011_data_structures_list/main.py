#In python there are 4 built in data structures
#List, tuple, Dictionary, sets

# LIST
#list allows mutability ->change in values after creation
#->allows duplicate values in list
#->Heterogenous, can store multiple data types in a list
#->Ordered can be accessed by positioning/indexing

#syntax
# a = [12, 13, 14, 15, "Pranav", True]
# a = [12, 13, 14, 15, 16, 24, 34.5]

#indexing
# print(a[0:4:1])#slicing like strings
# print(a[-1]) #reverse indexing also availabe like strings

# for i in range(len(a)):
#     print(a[i])

# for i in a: #This traversal cant access the index
#     print(i)

#onto the List methods-> methods are function defined in class
# print(dir(list)) #gives methods of list
# help(list)#explains methods

l = [1, 2, 3, 4, 5]

l.append(6) #this appends the object at end of list, like push_back
l.append(7)
l.append(8)

l.insert(1, 25) #takes (index, object), put the object at the given index
l.extend([9, 10, 11]) #append elements in bulk to the list at end

l.remove(3) #removes first occurence of element passed
l[0] = 10 #mutability, can be done in list, cant be on string
print(l)