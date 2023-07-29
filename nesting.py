# you can store multiple dictionaries in a list, or a list of items as a value in a dictionary

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
# a more realistic ex. would involve more than three alien with a code that automatically generates each alien.

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens:
    print(alien)
print("..")

print(f"Total number of aliens: {len(aliens)}")

# what if we want to change some aliens color, speed and points while the game progress

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)

print("..")


# A List in a Dictionary
# its usefull to put a list inside a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
    
    
# you can nest a list inside a dictionary multiple times

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskkkell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
        

# A Dictionary in a Dictionary
# you can nest a dictionary inside another dictionary

user = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einsten',
        'location': 'princeton',
    },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        
    },
}

for username, user_info in user.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation {location.title()}")