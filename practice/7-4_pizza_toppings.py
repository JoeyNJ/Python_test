promt = "\nEnter the pizza toppings you want! "
promt += "\nEnter 'quit' when you're finished. "

toppings = ""
while toppings != 'quit':
    toppings = input(promt)
    print(f"we will add {toppings.title()} to your pizza.")