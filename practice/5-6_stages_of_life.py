age = 3

if age < 2:
    person = 'baby'
elif age < 4:
    person = 'toddler'
elif age < 13:
    person = 'kid'
elif age < 20:
    person = 'teenager'
elif age < 65:
    person = 'adult'
else:
    person = 'elder'

print(f"The person's stage of life is {person}")