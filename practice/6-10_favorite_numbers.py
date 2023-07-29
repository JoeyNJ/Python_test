# use dictionary to print people's favorite number

favorite_num = {
    'joey': [24, 25],
    'joan': [2, 22],
    'nenita': [28, 45],
    'boy': [10, 7],
    'carding': [2, 22],
    }

for names, fav_num in favorite_num.items():
    print(f"\n{names.title()}'s favorite numbers are:")
    for num in fav_num:
        print(f"\t{num}")