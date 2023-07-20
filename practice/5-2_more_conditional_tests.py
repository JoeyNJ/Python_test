rat_friend = ['alive!']         # this code didn't work because I forgot the !
if 'alive!' in rat_friend:
    print("!!!!")
    
    
friends = ['rat', 'dog', 'cat', 'bird', 'African toad']
friend = friends[-1]
if friend.lower() == 'african toad':
    print("I wonder how is African toad doing now?")
    
    
if 2 == 2: print("2 is = to 2")
if 3 != 1: print("3 is not equal to 1")
if 4 > 2: print("4 is greater that 2")
if 1 < 2: print("1 is less than 2")
if 0 <= 1: print("0 is less than or equal to 1")
if 1 >= 1: print("1 is more than or equal to 1")


test = 1
wook = 2

if (test and wook) > 0:
    print("Lets wook!!")
    
    
key = 0
paw = 1

if key == 0 or paw == 0:
    print("Reeeeee")
    
    
pets = ['cats', 'dogs', 'birds', 'toads', 'rats']

if 'ducks' not in pets:
    print("There are no DUCKS")
    
    
pets = ['cats', 'dogs', 'birds', 'toads', 'rats']

if 'rats' in pets:
    print("MY RAT FRIEND!!")