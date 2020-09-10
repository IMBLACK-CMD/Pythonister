#for loop
#use len to know the number of entries in a list
#this code determines how many items are in the list
numbers = [6,5,4,3,8,9,3,6,8,2,6,7,8,9,1]
sum = 0
for val in numbers:
    sum = sum+val
    
print("Number of entries in a list: ", len(numbers))
print("The sum of all numbers is : ", sum)