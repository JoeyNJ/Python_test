# make a dictionary called favorite_places, think of 3 names to use as keys in the dictionary
# and store one to three favorite places for each person

favorite_places = {
    'joey': ['japan', 'teyvat', 'tungko'],
    'joan': ['japan', 'jolibee'],
    'joy': ['tungko'],
}

for name, favorite_place in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in favorite_place:
         print(f"\t{place.title()}")