programming_words = {
    'list': 'Is a collection of items in a particular order.',
    'tuple': 'Is a kind of list where you cannot change its values.',
    'if statements': 'Is where you check a condition and see if it is true or false to run a code.',
    'print()': 'Is a function in Python where you can display/print inside the parenthesis.',
    'dictionaries': 'Is a collection of key=value pairs.',
    'loop': 'is a term used to define a code where its specifically made to go in a loop',
    'method': 'are a kind of suffix function where you wrap them arround a variable and they will change the value based on the method used',
    'string': 'any characters surrounded by " " or '' ''',
    'white spaces': 'are spaces, tabs and newlines included in a string value',
    '#comments': 'to write a comment in your code use #comment in this line',
}

for words, meaning in programming_words.items():
    print(f"{words.title()}:\n\t{meaning}.\n")