#Annonymous or Lambda functions
#we use either filter() or map() together with lambda functions

#we are going to choose EVEN numbers from a list

my_list = [1,5,2,4,8,7,6,11,3,12,]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)

#using map() with lambda to double the numbers
new_list2 = list(map(lambda x:(x*2), my_list))
print(new_list2)