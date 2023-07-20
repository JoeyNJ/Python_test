# slicing a list
# animals[1:3] python will start on the 2nd item and stop at the 3rd
animals = ['cat', 'dog', 'bird', 'fish']
print(animals[1:3])

# players[0:3] will start on the first item and stop at the last item before the 3
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# if you ommit the first index in a slice, Python starts the slice at the beginning
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

# similarly if you ommit the last index, it will end at the last item on the list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:]) # Python returns all the items form the 3rd index through the end

# recall that negative index returns an item a certain distance from the end of the list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

# you can include a 3rd value in the brakkckets indicating a slice, it will skip that many items
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[: : 2]) # 1st and 2nd index are ommited telling it to use the whole list, 3rd index tells it to skip every 2 items