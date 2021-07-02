# Python’s filter() is a built-in function that allows you to process
# an iterable and extract those items that satisfy a given condition.
# This process is commonly known as a filtering operation.
# With filter(), you can apply a filtering function to an iterable and
# produce a new iterable with the items that satisfy the condition at hand.
# In Python, filter() is one of the tools you can use for functional programming.
import math


def is_positive(number):
    return number > 0


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


numbers = [-1, -2, 4, 5, -6, 9, 0, 21, 99, 23, 27, 17]
print('inital number:', numbers)
positive_numbers = list(filter(is_positive, numbers))
print('positive numbers:', positive_numbers)
prime_numbers = list(filter(is_prime, numbers))
print('prime numbers:', prime_numbers)

# using filter and map together
squared_prime = list(map(lambda x: x * x, filter(is_prime, numbers)))
print('square prime:', squared_prime)

twice_positive = list(filter(is_positive, map(lambda x: x * 2, numbers)))
print('twice prime:', twice_positive)
