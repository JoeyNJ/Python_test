#list is a collection of items in a particular order
#bicycles is a list: name = [1, 2, 3, 4, ...]
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#index :used to locate a content of a list based on order
#it starts with 0
#when asked for a single item, returns without square brackets
print(bicycles[0])
print(bicycles[3])

#can also be edited by methods
print(bicycles[2].title())

#index -1 :special syntax to access the last element in a list
#this extends to the other negative index values as well ex: -2 returns the 2nd, -3 returns the 3rd and so on
print(bicycles[-1])
print(bicycles[-2])

# you can use individual values from a list just as you would any other variable
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# modifiying list:  list[0] = new_value
motors = ['honda', 'yamaha', 'suzukki']
print(motors[0])
print(motors)
motors[0] = 'ducati'
print(motors)
print(motors[0])

# appending elements to the end of the list by .append
motors = ['honda', 'yamaha', 'suzukki']
print(motors)

motors.append('dugati')
print(motors)

# use .append to create a dynamic list from an empty list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzukita')
print(motorcycles)

# use .insert to add a new element at any position
motors = ['honda', 'yamaha', 'suzukki']

motors.insert(0, 'dugatisan')
print(motors)

# use del statement to remove an item if you know its index from a list
motors = ['honda', 'yamaha', 'suzukki']

del motors[0]
print(motors)

motors = ['honda', 'yamaha', 'suzukki']
del motors[1]
print(motors)

# use .pop() method to remove and work with that item
motors = ['honda', 'yamaha', 'suzukki'] 
print(motors)

popped_motors = motors.pop()
print(motors)
print(popped_motors)

# use .pop() to remove an item from any position by including its index
motorcycles = ['honda', 'yahama', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# use .remove() to remove an item from a list if you only know its value
motorcycles = ['honda', 'yahama', 'suzuki', 'dugati']
print(motorcycles)

motorcycles.remove('dugati')
print(motorcycles)

# you can also use .remove() to work with the value that's being removed from the list
motorcycles = ['honda', 'yahama', 'suzuki', 'dugati']
print(motorcycles)

too_expensive = 'dugati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")