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


#Simple if Statements
#has one test and one action:

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")   # you can add as many lines of code indented to be executed
    # if the value of age is less than 18, this will produce nothing
    
#if-else Statements
# similar to if statemens,k but else statement define an action to execute when the condition fails

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    
#if-elif-else Chain
# to test more than 2 situations, only executes 1 block in an if-elif-else chain:

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
    
# rather than printing the admission price within the block, its more concise to print after the chain evaluated:

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
    
print(f"Your admission cost is ${price}.")

#Using multiple elif Blocks:
# you can use as many elif blocks in you code:

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age > 65:   # else block can be ommited, but the blocks must atleast pass one test to execute the print call:
    price = 20
    
print(f"Your admission cost is ${price}.")

#Testing Multiple Conditions
# use a series of simple if statements w/ no elif or else blocks:

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!")

#Summary: if you want only one block of code to run, use an if-elif-else chain.
#If more than one block of code needs to run, use a series of independent if statements


#Checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("Finished making your pizza!")

#What if we run out of green peppers?
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
        
print("\nFinished making your pizza!")


#What if the list is empty;
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    
    
#Using multiple list;
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")
        
print("\nFinished making your pizzza!")