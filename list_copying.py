# to copy a list you can make a slice that includes the entire original list by ommiting the 1st and 2nd index
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:] # here we make a new list called friends_foods, we make its value by making a copy of my_foods by asking for a slice of it without the indices

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

# to prove that we actually have two separate lists, we'll add a new food to each list and show that each list keeps track of the appropriate person's foods
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

# if instead we store a copy of my_foods in friend_foods and set friend_foods equal to my_foods items will appear on both the same
my_foods = ['pizza', 'falafel', 'carrot cake']
# this doesn't work:
friends_foods = my_foods

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)