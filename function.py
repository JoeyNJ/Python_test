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
    