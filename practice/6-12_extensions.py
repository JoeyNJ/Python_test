family_guests = ['mother', 'father', 'sister', 'uncle', 'aunty']
print(f"Hello everyone! I would like to inform you that the total number of attendies are {len(family_guests)}!")

for family in family_guests:
    print(f"Hello {family} If you are free this weekend, could you give time to a dinner that I prepared for an occasion!")

# someone has other plans and can't attend
print(f"Unfortunately {family_guests[-1].title()} can't attend the dinner, since we have a free seat I will invite a cousin.")

family_guests[-1] = 'cousin'
print(family_guests)

for family in family_guests:
    print(f"Hi {family.title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!")


# I found a bigger table! I will invite another family
print("For all attendies on the dinner party I have good news! We have found a place with a bigger table so I will invite another family member!")

family_guests.insert(0, 'joan')
family_guests.insert(3, 'nanay')
family_guests.insert(-1, 'tatay')

print(family_guests)

for family in family_guests:
    print(f"Hi {family.title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!")
# Unfortunately again the place I got was demolished! I now only invite two family members!
print("Unfortunately again the place I got was demolished! I now only invite two family members!")

print(family_guests)

for family in family_guests:
    family_guests.pop()
    if family != 'nanay' or 'joan':
        print(family_guests)
# My only two family members are left

print("I still have my Nanay and Joan")