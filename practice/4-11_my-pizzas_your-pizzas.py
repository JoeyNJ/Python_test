pizzas = ['pineapple', 'ballonee', 'overload']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")

print("\nI really like pizza!")

friend_pizzas = pizzas[:]

pizzas.append('macaroni')
friend_pizzas.append('hotdog')

print("My favorite pizzas are:")
for my_pizzas in pizzas:
    print(f"\t{my_pizzas.title()}")
    
print("\nMy friend's favorite pizzas are:")
for friends_favorite_pizzas in friend_pizzas:
    print(f"\t{friends_favorite_pizzas.title()}")