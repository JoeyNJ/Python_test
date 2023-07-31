# input() function ex: ff ask the user to enter some text then displays it back to the user

#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

# writing clear promtps

#name = input("Please enter your name: ") # add a space at the end of your promt
#print(f"\nHello, {name}!")

# assign a variable to your promt to display more promt with more lines

#prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt += "\nWhat is your first name? "

#name = input(prompt)
#print(f"\nHello, {name}!")

# Use int() to accept numerical input

#age = input("How old are you? ")
#age = int(age)
#if age >= 18: print(age)


# How to use the int(), a program that determinees whether people are tall enough to ride a roller coaster:

#height = input("How tall are you, in inches? ")
#height = int(height) # if you use numerical input to do calculations and comparisons, convert the input value to int()

#if height >= 48:
#    print("\nYou are tall enough to ride!")
#else:
#    print("\nYou'll be able to ride when you're a little older.")
    
# The Modulo Operator
# even or odd

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")