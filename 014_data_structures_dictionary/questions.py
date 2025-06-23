#Q1 merge two dictionaries
# help(dict)

a = {10: 100, 20: 200, 30: 300, 40: 400, 50: 500}
b = {30: 1000, 60: 600, 70: 700, 80: 800}

# answer 1

# a.update(b)
# print(a.items())

# answer 2

for i in b:
    a[i] = b[i]

print(a)

#Q2 sum all values in the dictionary

sum_dict_a = 0

for i in a:
    sum_dict_a += a[i]

print("Sum of all item in dictionary a: ", sum_dict_a)    

#Q3 count frequency of each element in a list

randomList = [1,1, 1, 2, 3, 4, 5, 2, 2, 4, 3, 5, 5]

freqDictionary = {}

for i in randomList:
    if i in freqDictionary.keys(): #checks if a key-value pair of i as key exist in dictionary, if yes add 1 in frequency of i
        freqDictionary[i] += 1
    else:
        freqDictionary[i] = 1

print(freqDictionary)

#Q4 

d1 = {10: 100, 20: 200, 30: 300}
d2 = {30: 300, 60: 600, 70: 700}
#combine but not replace duplicates, add them

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)