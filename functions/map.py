# Map takes a transforming function and apply
# Python’s map() is a built-in function that allows you to process and
# transform all the items in an iterable without using an explicit for
# loop, a technique commonly known as mapping. map() is useful when you
# need to apply a transformation function to each item in an iterable and
# transform them into a new iterable. map() is one of the tools that support
# a functional programming style in Python.

def square(number):
    return number * number


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print('square numbers:', squared_numbers)
