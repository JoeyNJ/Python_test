# if statements: here we want to print bmw in all caps, using a for loop to print all
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        

# Conditional Tests: checking for equality
car = 'bmw'     # this sets the car value to 'bmw'
car == 'bmw'    # this checks if the car is equal to 'bmw'
True

# Ignoring Case when checking for equality
# Python equality test is case sensitive
car = 'Audi'
car == 'audi'
False

# Convert the variable's value to lowercase before doing the comparisons:
car = 'Audi'
car.lower() == 'audi'
True


# Checking for Inequality: (!=)
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!") 
    

# Numerical Comparisions:
age = 18
age == 18
True

# check if two numbers are not equal
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

# you can include various mathematical comparisons in your conditional statements
age = 19
age < 21
True

age <= 21
True

age > 21
False

age >= 21
False


# Checking Multiple Conditions:
# using and to check if multiple conditions are both true
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >=21
False

age_1 = 22
age_0 >= 21 and age_1 >= 21
True

# using or to check if multiple conditions passes when either or both of the individual tests pass
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >=21
True

age_0 = 18
age_0 >= 21 or age_1 >=21
False


# Checking whether a Value is in a list
# using the keyword in
requested_toppings = ['mushrooms', 'onions', 'pineapple']

'mushrooms' in requested_toppings
'peperoni' in requested_toppings

# Checking whether a Value is NOT in a list
# using the keyword not
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    
# Boolean Expressions
game_active = True
can_edit = False