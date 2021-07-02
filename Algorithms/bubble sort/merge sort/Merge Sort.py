def merge(arr, left_index, middle_index, right_index):
    """
    sorts the array in descending order
    change left_half[i] <= right_half[j] to left_half[i] >= right_half[j] for sorting in descending order
    """
    n1 = middle_index - left_index + 1
    n2 = right_index - middle_index

    # create temp arrays
    left_half = [0] * n1
    right_half = [0] * n2

    # copy data to temp arrays left and right
    for i in range(0, n1):
        left_half[i] = arr[left_index + i]
    for j in range(0, n2):
        right_half[j] = arr[middle_index + 1 + j]

    # merge the temp arrays back into arr[left..right]
    i = 0  # initial index of first subarray
    j = 0  # initial index of second subarray
    k = left_index  # initial index of merged subarray

    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    # copy the remaining elements of left, if there are any
    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1
    # copy the remaining elements of right, if there are any
    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1


def merge_sort(arr, left_index, right_index):
    """
    :param arr: array of numbers
    :param left_index:left index
    :param right_index:right index
    """
    if left_index < right_index:
        # same as (l + r)//2, but avoids overflow for large l and h
        middle_index = (left_index + (right_index - 1)) // 2

        # sort first and second halves
        merge_sort(arr, left_index, middle_index)
        merge_sort(arr, middle_index + 1, right_index)
        merge(arr, left_index, middle_index, right_index)


numbers = [12, 11, 4, 1, 9, 0, 16]
print('before sorting:', numbers)
merge_sort(numbers, 0, len(numbers) - 1)
print('after sorting:', numbers)
