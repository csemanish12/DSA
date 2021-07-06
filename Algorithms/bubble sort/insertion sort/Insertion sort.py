# The insertion sort, although still O(n2), works in a slightly different way.
# It always maintains a sorted sublist in the lower positions of the list.
# Each new item is then “inserted” back into the previous sublist such that the
# sorted sublist is one item larger.
# We begin by assuming that a list with one item (position 0) is already sorted.
# On each pass, one for each item 1 through n−1, the current item is checked
# against those in the already sorted sublist.
# As we look back into the already sorted sublist,
# we shift those items that are greater to the right.
# When we reach a smaller item or the end of the sublist,
# the current item can be inserted.

import timeit


def insertion_sort():
    array = [11, 5, 2, 1, 0, 9, 10, 16, 4]
    for i in range(0, len(array) - 1):
        for j in range(i + 1, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]


def insertion_sort_while():
    array = [11, 5, 2, 1, 0, 9, 10, 16, 4]
    for i in range(1, len(array)):
        while array[i] < array[i - 1] and i > 0:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1


def insertion_sort_v2():
    array = [11, 5, 2, 1, 0, 9, 10, 16, 4]
    for index in range(1, len(array)):

        currentvalue = array[index]
        position = index

        while position > 0 and array[position - 1] > currentvalue:
            array[position] = array[position - 1]
            position = position - 1

        array[position] = currentvalue


number1 = [11, 5, 2, 1, 0, 9, 10, 16, 4]
number2 = [11, 5, 2, 1, 0, 9, 10, 16, 4]
print(timeit.timeit(insertion_sort, number=1000000))
print(timeit.timeit(insertion_sort_while, number=1000000))
print(timeit.timeit(insertion_sort_v2, number=1000000))
