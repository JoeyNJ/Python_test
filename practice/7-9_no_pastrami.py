sandwich_orders = ['cheese sandwich', 'ham sandwich', 'pastrami sandwich', 'pastrami sandwich', 'chicken sandwich', 'hotdog sandwich', 'pastrami sandwich']
finished_sandwiches = []

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
    print(sandwich_orders)
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order}.")
    
    finished_sandwiches.append(sandwich_order)

for finished_sandwich in finished_sandwiches:
    print(f"Here are all the finished sandwiches: \n{finished_sandwich.title()}")