# A simple Dictionary:
# a dictionary in python is a collection of key-value pairs.

alien_0 = {'color': 'green', 'points': 5} # the key here is color and its value 'green'


# accessing values in a dictionary
# give the name of the dictionary and place the key inside a set of square brackets:

alien_0 = {'color': 'green'}
print(alien_0['color'])

# you can access either color or the point value of alien_0:

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")


# Adding new key-value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#NOTE: As of Python 3.7 dictionaries retain the order in whick they were defined


# Starting with an Empty Dictionary
# it's sometimes convenient or even necessary to start with an empty dictionary:

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)


# Modifitying Vaues in a Dictionary
# we might want to give a key a new value as the program progresses

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


# for a more interesting ex: let's track the position of an alien that can move at dif. speeds

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}.")

# Move the alien to the right
# Determine how far to move the alien based on its current speed

# To turn the medium-speed alien to a fast one you would add:
# modify the value of 'speed'

#NOTE: alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3 # This must be a fast alien
    
# The new position is the old position + the increment

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}.")


# Removing Key-value pairs:
# by using del

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points'] #NOTE: This line deletes the key and its value 'points' permanently.
print(alien_0)


# A dictionary of Similar Objects:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

# Using get() to Access Values

alien_0 = {'colors': 'green', 'speed': 'slow'}
#print(alien_0['points']) #NOTE: KeyError

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
print(alien_0['points'])