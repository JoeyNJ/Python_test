basic_foods = ('fried chicken', 'rice', 'pancit', 'palabok', 'sopas')
print("This buffet only serves five basic foods:")
for basic_food in basic_foods:
    print(f"{basic_food.title()}")
    
#basic_foods.append('egg')

print("\nThe buffet changes its last two items with 'adobo' and 'spagetti'")
basic_foods = ('fried chicken', 'rice', 'pancit', 'adobo', 'spagetti')
for basic_food in basic_foods:
    print(f"{basic_food.title()}")