# make 3 dif. exits

promt = "\nEnter the pizza toppings you want! "
promt += "\nEnter 'quit' when you're finished. "

toppings = ""
active = True
while active:
    toppings = input(promt)
    if toppings == 'quit':
        active = False
    else:
        print(f"we will add {toppings.title()} to your pizza.")