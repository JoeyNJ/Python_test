# example of a simple function

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# Passing info to a Function

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

# Positional Arguments

def describe_pet(animal_type, pet_name):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# Multiple Function Calls

describe_pet('dog', 'willie')
describe_pet('cat', 'tiger')

# Order matters in positional arguments

describe_pet('harry', 'hamster')

# Keyword Arguments

def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(animal_type='hamster', pet_name='harry') # this is much better
describe_pet(pet_name='harry', animal_type='hamster') # oder doesn't matter

# Default values
# you can set a default value if an argument is not available

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(pet_name='willie') # python still considers this a positional arguments
describe_pet(pet_name='harry', animal_type='hamster')

# Equivalent Function Calls

# a dog named Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# a hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# Avoiding Argument Errors

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
#describe_pet() here's a missing information


# Return Values

# returning a simple value

def get_formated_name(first_name, last_name):
    """Return a full name, neatly formated."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formated_name('jimi', 'hendrix')
print(musician)

# Making an Argument Optional
# here if we wanted to add a middle name we can

def get_formated_name(first_name, middle_name, last_name):
    """Return a full name, neatly formated."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formated_name('jonh', 'lee', 'hooker') # will give error if one is missing
print(musician)

# set default value of the middle_name to an empty string and move it to the end

def get_formated_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formated."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formated_name('jimi', 'hendrix')
print(musician)
musician = get_formated_name('john', 'hooker', 'lee')
print(musician)

# Returning a Dictionary

def build_person(first_name, lastname):
    """Return a dictionary of information about a persion."""
    person = {'first': first_name, 'last': lastname}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


# here you can add a optional information age
def build_person(first_name, lastname, age=None):
    """Return a dictionary of information about a persion."""
    person = {'first': first_name, 'last': lastname}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=56)
print(musician)


# Using a Function with a while loop

def get_formatted_name(first_name, last_name):
    """Return a fll name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' anytime to quit.)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")