# while loops runs as long as, or while, a certain condition is true

#current_number = 1
#while current_number <= 5:
#    print(current_number)
#    current_number += 1
    
# parrot.py

#promt = "\nTell me something, and I will repeat it back to you:"
#promt += "\nEnter 'quit' to end the program. "
#
#message = ""
#while message != 'quit':
#    message = input(promt)
#    if message != 'quit':
#        print(message)
        
        
# using a flag 

#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt = "\nEnter 'quit' to end the program. "
#
#active = True
#while active:
#    message = input(prompt)
#    
#    if message == 'quit':
#        active = False
#    else:
#        print(message)
        

# Using break to exit a Loop: exit a loop immediately without running any remaining code in the loop
# cities.py

#prompt = "\nPlease enter the name of a city you have visited:"
#prompt += "\n(Enter 'quit' when you are finished.) "

#while True: # while loops with while true will forever run unless it reaches a break statement
#    city = input(prompt)
#    
#    if city == 'quit':
#        break
#    else:
#        print(f"I'd love to go to {city.title()}!")
        
# Using continue in a loop: to return to the beggining of the code

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# Avoiding Infinite Loops

x = 1
while x <= 5:
    print(x)
    x += 1
