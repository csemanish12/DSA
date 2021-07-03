# Python is famous for allowing you to write code that’s elegant,
# easy to write, and almost as easy to read as plain English. One of
# the language’s most distinctive features is the list comprehension, which you can use to create powerful
# functionality within a single line of code.

# squared numbers
squares = [i * i for i in range(10)]
print(squares)

# new_list = [expression for member in iterable]

# list comprehension are often described as being more pythonic than loops or map
# we can use it for both filter as well as map
# This is the main reason why list comprehensions are considered Pythonic, as Python embraces simple,
# powerful tools that you can use in a wide variety of situations

# using conditional logic

# using conditional logic at the end to filter out things
# new_list = [expr for member in iterable (if conditional)]
sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
print('vowels:', vowels)


# moving conditional logic in separate function
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels


consonants = [i for i in sentence if is_consonant(i)]
print('consonants:', consonants)

# using conditional in the middle to change the things
# new_list = [expr (if conditional) for member in iterable]

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0for i in original_prices]
print('prices:', prices)
