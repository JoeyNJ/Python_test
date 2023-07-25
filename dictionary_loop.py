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