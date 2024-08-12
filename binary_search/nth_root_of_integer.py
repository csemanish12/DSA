"""
Problem statement
You are given two positive integers 'n' and 'm'. You have to return the 'nth' root of 'm', i.e. 'm(1/n)'. If the 'nth root is not an integer, return -1.



Note:
'nth' root of an integer 'm' is a number, which, when raised to the power 'n', gives 'm' as a result.


Example:
Input: ‘n’ = 3, ‘m’ = 27

Output: 3

Explanation:
3rd Root of 27 is 3, as (3)^3 equals 27.

"""


# TC = 0(log2n * log2n)
# SC = O(1)

def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        exponent = get_exponent(mid, n, m)
        if exponent == 1:
            return mid
        elif exponent == 0:
            low = mid + 1
        elif exponent == 2:
            high = mid - 1
    return -1


def get_exponent(mid, n, m):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * mid

        if ans > m:
            return 2

    if ans == m:
        return 1
    else:
        return 0


n = 3
m = 27
print("ans", NthRoot(3, 27))
