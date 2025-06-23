#Hashmap in python: Dictionary

#Syntax

d = {}
e = {1 : "hello"} #dictionary consists key value pairs

print(type(d)) #not set but dictionary
print(e)

#PROPERTIES
#->mutable: allowed
#->dulplicates in value is allowed, but keys shold always be unique
#->Ordered: dictionary follows insertion order
#->Heterogenous nature

dic = {10: 100, 20: 200, 30: 300, 40: 400}

print(dic[40]) #not index but keys
dic[10] = 1000 #values can be updated but not keys
print(dic)

# dic.update({50: 500})
#or you can write
dic[50] = 500
print(dic)

del dic[30] #deleting key
print(dic)

#dictionary traversing
for i in dic:
    print(i, dic[i]) #iteration is over keys


#traverse directly on values
for j in dic.values():
    print(j)

# help(dict)
dic.clear()
print("Dictionary cleared: ", dic)

#deep copy vs shallow copy

a = [1, 2, 3, 4, 5]
b = a
b[0] = 100
print("list a: ", a) #output: [100, 2, 3, 4, 5]
#this was a deep copy, any change in copy is reflected on orignal

#shallow copy below
c = a.copy() #this is a shallow copy, any change does not reflect on orignal
c[3] = 500
print("a: ", a)
print("c: ", c)

dictionaryII = {10: 100, 20: 200, 30: 300}

d2 = dictionaryII.get(20) #returns the value at given key
print("d2: ", d2) 

print(dictionaryII.items())
poppedElement = dictionaryII.pop(10)
print(poppedElement)
print(dictionaryII)