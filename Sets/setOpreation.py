# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(type(A))
print(type(B))

#Union
my_set = A|B
print(my_set)

#Intersection
diff_setA = A - B
print(diff_setA)
diff_setB = B - A
print(diff_setB)


