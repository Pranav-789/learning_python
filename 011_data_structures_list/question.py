# QUESTIONS ON LIST

l = [-45, 67, 12, -68, -69, 34]
# l = [12, 13, 14, 15, 16, 17, 18, 19, 20]

#Q1. print all positive and negative elements in the list l

print("Positive numbers: ")
for i in range(len(l)):
    if(l[i] >= 0):
        print(l[i])

print("Negative numbers: ")
for i in range(len(l)):
    if(l[i] < 0):
        print(l[i])

    

#Q2.Mean of list elements or average
listSum = 0
for i in l:
    listSum += i

mean = listSum/len(l)

print("Mean of list l: ", l, " is ",mean)

#Q3. find greatest element and print it's index, II finding second greatest
greatest = l[0]
greatest_index = 0
secGreatest = l[0]
SecGreatest_index= 0
for i in range(len(l)):
    if(l[i] > greatest):
        secGreatest = greatest
        SecGreatest_index = greatest_index
        greatest = l[i]
        greatest_index = i
    elif(l[i] > secGreatest and l[i] < greatest):
        secGreatest = l[i]
        SecGreatest_index = i

print(f"The greatest element in list is {greatest} at index {greatest_index}")
print(f"The Second greatest element in list is {secGreatest} at index {SecGreatest_index}")

#Q4 check if list is sorted or not
def isGreater(a, b):
    if(a >= b):
        return True
    else:
        return False
    
for i in range(len(l)-1): #used -1 because if only len(l) i+1 will throw out of bound error
    if (not(isGreater(l[i+1], l[i]))):
        print("The list is not sorted")
        break
else: #this else is connected with for loop, executed when break is not executed inside the loop
    print("The list is sorted")