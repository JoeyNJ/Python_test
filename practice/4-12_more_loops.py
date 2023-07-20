my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for my_favorite_foods in my_foods:
    print(f"\t{my_favorite_foods.title()}")

print("\nMy friend's favorite foods are:")
for friends_favorite_food in friend_foods:
    print(f"\t{friends_favorite_food.title()}")