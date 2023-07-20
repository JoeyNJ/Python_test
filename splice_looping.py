# use slice in a for loop to loop through a subset of elements in a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player  in players[:3]: # only the first 3 players are being used here
    print(player.title())