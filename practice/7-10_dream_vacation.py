responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which place is your dream vacation? ")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
print("\n--- Polling Result ---")
for name, response in responses.items():
    print(f"{name.title()}'s dream vacation is on {response.title()}.")