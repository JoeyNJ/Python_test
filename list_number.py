# range() here generate a series of numbers
# in this ex. it only prints 1,2,3,4: because Python starts at 0
for value in range(1, 5):
    print(value)
    
# to print 1-5 
for value in range(1, 6):
    print(value)

# you can also pass range() only one argument
# it will start the sequence at 0
for value in range(6):
    print(value)
    
# list(range(*, *)) will make a list of numbers in range
numbers = list(range(1, 6))
print(numbers)

# you can also use range() to skip numbers
# if you pass a 3rd argument to range()
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# in this ex. the range() function starts with 2 and adds 2 to that value untill it reaches or passes 11

# you can create almost any set of numbers using range()
# here how you might put the first 10 square numbers into a list
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
# you can write this code more concisely by ommiting the temporary variable square and appending the new value directly
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

# simple statistics with a list of numbers: min(), max(), sum()
digits = []
for value in range(10):
    digit = value
    digits.append(digit)
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)