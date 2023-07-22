current_users = ['admin', 'Jade', 'ken', 'carol', 'fred']

new_users = ['desmond', 'paula', 'pauline', 'arcueid', 'JADE']

lower_current_users = [current_user.lower() for current_user in current_users]

print(lower_current_users)

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print(f"{new_user} is already in use.")
    else:
        print(f"{new_user} is available.")