#SET data structure

#syntax
s = {1, 8, 9, 2, 3, 4, 5}

#PROPERTIES
#-> mutable: allowed
#-> duplicates: not allowed
#-> unordered: indexing not available
#-> semi-heterogenous, can store strings, numbers, tuples but not everything
#it stores only immutable objects

a = hash("hello")
print(a) #this is the hash value that set uses to store elements

c = hash((1, 2, 344)) 

print(c)

#set traversing, only one method, always give random values
print("Set traversal")
for i in s:
    print(i)

#set methods
b = {1, 2, 3}

b.remove(2) #remove or discord
print(b)

# b.clear()#removes all element from set
# print(b)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union_set = A.union(B)
print("Union by method: ", union_set)
#or you can write
print("Union by pipe: ",A|B)


intersection_set = A.intersection(B)
print("Intersection by method: ",intersection_set)
print("Intersection by &: ", A&B)

difference_set = A.difference(B)
print("Difference by method: ", difference_set)
print("Difference by - : ", A-B)

# simmilary simitric difference will be A.symmetric_difference(B)
print("Symmetric difference: ", A^B)

#Compound operation for above can be directly applied on set as follows
B-=A
print(B)