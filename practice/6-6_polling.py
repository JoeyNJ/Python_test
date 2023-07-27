# make a list of people who participated in the pole and people who did not, compare both by printing dif. messages to each

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['jen', 'sarah', 'edward', 'phil', 'jason', 'ren', 'arcuied',]

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you for responding on the poll {person.title()}.")
    if person not in favorite_languages.keys():
        print(f"Please take the poll {person.title()}.")