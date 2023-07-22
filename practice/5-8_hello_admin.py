usernames = ['admin', 'jade,', 'ken', 'carol', 'fred']

for username in usernames:
    if username == 'admin':
        print(f"Hello Sir.{username.title()}, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for loggin in again.")