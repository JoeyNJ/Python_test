seating = input("How many people are in your dinner group? ")
seating = int(seating)

if seating > 8:
    print(f"\nSorry for that, you will have to wait for a table.")
else:
    print(f"\nThe table is ready!")