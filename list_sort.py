# .sort() method sort's the list in alphabetical order
# this permanently changes the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# reverse=true argument on the .sort() method reverse the sort order of the list
# this permanently changes the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# sorted() function to temporary sort a list
# can also accept the reverse=True function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# .reverse method reverse the original order of the list, not aphabetically buy chronological order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
# .reverse() changes the list permanently but you can still revert to the original by using it again

# len() function finds the length of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)