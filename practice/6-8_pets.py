# make dictionaries that represents different pets, in each include
# the kind of animal and the owner's name. Store them in a list pets

cat = {
    'kind': 'cat',
    'pet_name': 'tama',
    'owner_name': 'touka',
}
dog = {
    'kind': 'dog',
    'pet_name': 'inui',
    'owner_name': 'malenia',
}
fish = {
    'kind': 'fish',
    'pet_name': 'kok',
    'owner_name': 'lumine',
}

pets = [cat, dog, fish]

for pet in pets:
    print(f"{pet['owner_name'].title()} has a pet {pet['kind']} named {pet['pet_name'].title()}.")