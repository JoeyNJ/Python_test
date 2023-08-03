sandwich_orders = ['cheese sandwich', 'ham sandwich', 'chicken sandwich', 'hotdog sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order}.")
    
    finished_sandwiches.append(sandwich_order)

for finished_sandwich in finished_sandwiches:
    print(f"Here are all the finished sandwiches: \n{finished_sandwich.title()}")