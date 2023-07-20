# tuple is a list that value you can't change

dimension = (200, 50)
print(dimension[0])
print(dimension[1])

# see if you change the value of dimension
# this will give a TypeError
#dimension[0] = 250

#Note: tuples are defined by a comma, if you want to define a tuple with one element you need to add a trailing comma
my_t = (3,)

# you can loop over all values in a tuple using a for loop
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
    
# Writting over a tuple: you can't modify a tuple so you need to assign a new value to a variable that represents a tuple
# If we want to change values we can redefine the entire tuple:
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    
# tuples are simple data structures, use them when you want to store a set of values that should not be changed throughout the life of a program