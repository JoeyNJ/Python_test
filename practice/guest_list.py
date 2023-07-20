family_guests = ['mother', 'father', 'sister', 'uncle', 'aunty']
print(f"Hello everyone! I would like to inform you that the total number of attendies are {len(family_guests)}!")

message = f"Hi {family_guests[0].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[1].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[2].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[3].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[4].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

# someone has other plans and can't attend
print(f"Unfortunately {family_guests[-1].title()} can't attend the dinner, since we have a free seat I will invite a cousin.")

family_guests[-1] = 'cousin'
print(family_guests)

message = f"Hi {family_guests[0].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[1].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[2].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[3].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[4].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

# I found a bigger table! I will invite another family
print("For all attendies on the dinner party I have good news! We have found a place with a bigger table so I will invite another family member!")

family_guests.insert(0, 'joan')
family_guests.insert(3, 'nanay')
family_guests.insert(-1, 'tatay')

print(family_guests)

message = f"Hi {family_guests[0].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[1].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[2].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[3].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[4].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[5].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[6].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

message = f"Hi {family_guests[7].title()}, If you are free this weekend, could you give time to a dinner that I prepared for an occasion!"
print(message)

# Unfortunately again the place I got was demolished! I now only invite two family members!
print("Unfortunately again the place I got was demolished! I now only invite two family members!")

canceled_invitee = family_guests.pop().title()
print(f"Hellok {canceled_invitee} unfortunately we can't invite you to dinner, SORRY!!!")
canceled_invitee = family_guests.pop().title()
print(f"Hellok {canceled_invitee} unfortunately we can't invite you to dinner, SORRY!!!")
canceled_invitee = family_guests.pop().title()
print(f"Hellok {canceled_invitee} unfortunately we can't invite you to dinner, SORRY!!!")
canceled_invitee = family_guests.pop().title()
print(f"Hellok {canceled_invitee} unfortunately we can't invite you to dinner, SORRY!!!")

canceled_invitee = family_guests.pop(1).title()
print(f"Hellok {canceled_invitee} unfortunately we can't invite you to dinner, SORRY!!!")
canceled_invitee = family_guests.pop(1).title()
print(f"Hellok {canceled_invitee} unfortunately we can't invite you to dinner, SORRY!!!")

# My only two family members are left

print(f"Hi {family_guests[0].title()}, I am happy to tell you that you are one of the two lucky ones to attend the dinner!")
print(f"Hi {family_guests[1].title()}, I am happy to tell you that you are one of the two lucky ones to attend the dinner!")

del family_guests[0]
del family_guests[0]

print(family_guests)
print("I still have my Nanay and Joan")