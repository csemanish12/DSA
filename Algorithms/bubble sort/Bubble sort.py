def bubble_sort(numbers):
    """
    Sort list of numbers in descending order.
    Change the condition to numbers[i]>numbers[j] to sort the numbers in ascending order
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]  # swap the numbers


number = [1, 9, 3, 2, 5, 7]
print('Numbers before sorting:', number)
bubble_sort(number)
print('Number after sorting', number)


