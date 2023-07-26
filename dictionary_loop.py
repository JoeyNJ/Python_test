# Looping to all Key-Value Pairs"

# this is an examle of a dictionary containing a user's info

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items(): # create 2 variable names that will hold the key and value and use .items() to return the key-value pairs
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
    
# looping through all key-value pairs is usefull if you need both the key and value.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
    
# Looping through All the Keys in a Dictionary
# use .key() method to see only the keys

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys(): # Looping through keys is the default behaviour in looping through dictionary
    print(name.title())


# if a name matches one of our friends we display a message about their favorite language  
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
        
        
# you can use .keys() to find out if a particular person was polled
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    

# Looping Through a Dictionary's Keys in a Particular Order
# you can use sorted() function to get a copy of the keys in order:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()): #wrap sorted() on favorite_languages.keys() get a copy of the keys in order
    print(f"{name.title()}, thank you for thaking the poll!")
    
    
# Looping Through all Values in a Dictionary
#use the values() method to return a list of values without any keys
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned.")
for language in favorite_languages.values(): # for statement pulls all the values and assigh them to language
    print(language.title())

# this pulls all values w/o checking for repeats
# in a very long poll this will make the result repetitive
# set can be used to store a collection which each item must be unique:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): # when you wrap set() in a list that contains duplicate items, Python identifies the unique items in the list and builds a set from those
    print(language.title())
    

#NOTE: you can build a set directly using braces and seperating with commas:
languages = {
    'python',
    'ruby',
    'python',
    'c',
}
print(languages)
# it's easy to mistake sets for a dictionary, if you see a list wrapped in braces but with no key-value pairs, its a set