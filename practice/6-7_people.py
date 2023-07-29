joan_info = {
    'first_name': 'joan',
    'last_name': 'nicolas',
    'age': 22,
    'city': 'bulacan',
    }

joey_info = {
    'first_name': 'joey',
    'last_name': 'nicolas',
    'age': 28,
    'city': 'bulacan',
    }

nenita_info = {
    'first_name': 'nenita',
    'last_name': 'nicolas',
    'age': 45,
    'city': 'bulacan',
    }

family = [joan_info, joey_info, nenita_info]

for fam in family:
    print(f"Family member name: {fam['first_name'].title()}")
    first_name = f"{fam['first_name']}"
    last_name = f" {fam['last_name']}"
    full_name = first_name + last_name
    
    fam_age = f"{fam['age']}"
    
    print(f"Full name: {full_name.title()}, age: {fam['age']}, location: {fam['city'].title()}")