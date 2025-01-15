"""
What is Lower Bound?
The lower bound algorithm finds the first or the smallest index in a sorted array 
where the value at that index is greater than or equal to a given key i.e. x.

The lower bound is the smallest index, ind, where arr[ind] >= x. 
But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.

example:
array = [1,2,2,3]
target = 2
index 1 is the smallest index where arr[ind] >=x
"""
def lowerBound(arr: list[int], n: int, x: int) -> int:
    # Write your code here
    low = 0
    high = n -1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans


sample = [1,2,2,3]
target = 2
expected_ans = 2
ans = lowerBound(sample, len(sample), target)
assert expected_ans == ans, f"expected: {expected_ans} did not match actual: {ans}"