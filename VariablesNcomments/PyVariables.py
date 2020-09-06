import constants
#Variables are named locations that store data in memory
#example
number = 10

print("This is Number ", number)

#assigning multiple variables the same value
a,b,c = 1,2,"validate"
print(a)
print(b)
print(c)

#constants
print("..... constants......")
print(constants.PI)
print(constants.GRAVITY)
print("....Literal Collections.....")
officeEquip = ["laptops","desktop","files"]
print("this is a list :\n ", officeEquip)
print("turples:")
numbers=(1,2,3,4,5)
print("\n", numbers)
print("Dictionaries:")
bio = {'fname':'Nelson','lname':'Ongiti','subject':'python variables'}
print(bio)
print("set:")

tableFields = {'fname','lname','dob',}
print(unsorted(tableFields))
