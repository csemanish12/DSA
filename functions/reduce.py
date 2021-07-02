# Another functional programming tool in Python is reduce().
# Unlike filter() and map(), which are still built-in functions,
# reduce() was moved to the functools module. This function is useful
# when you need to apply a function to an iterable and reduce it to a
# single cumulative value. This kind of operation is commonly known as a
# reduction or folding.

# reduce(function, iterable, initial)
# function: holds any python callable that accepts two arguments and returns a single value
# iterable: holds any python iterable
# initial: holds a value that serves as a starting point for the first partial computation or reduction.
# it is optional

# A call to reduce starts by applying function to the first two items in iterable.
# This way it computes first cumulative result, called an accumulator.
# Then reduce uses accumulator and the second item in iterable to computer the next
# cumulative result. The process continues until the function returns with single value


from functools import reduce


def number_sum(number1, number2):
    return number1 + number2


def is_even(number):
    return number % 2 == 0


def square(number):
    return number * number


numbers = [1, 2, 3, 4, 5, 5, 6, 7]
sum_of_numbers = reduce(number_sum, numbers)
print('sum of numbers is:', sum_of_numbers)

# using reduce and filter
sum_of_even_numbers = reduce(number_sum, filter(is_even, numbers))
print('sum of even numbers is:', sum_of_even_numbers)

# using reduce and map
sum_of_square_numbers = reduce(number_sum, map(square, numbers))
print('sum of squared number:', sum_of_square_numbers)
