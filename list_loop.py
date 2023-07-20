# in a list using for temp_var in list:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
# can also do more in a loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

# forgeting to indent
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# logical error: forgetting to indent a line in a for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}!\n")

# indenting unnecessarily:
message = "Hello Python World!"
print(message)# if you indent this line it will give an error

# indenting unnecessary after the loop
# you can indent a code at the last line of the loop and make it also a part of the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}!\n")
    
    print(f"Thank you everyone, that was a great show!") # <<<<< This indentation
    
# forgetting the colon will give: SyntaxError: expected ':'
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)