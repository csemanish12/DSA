"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.



Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"


Constraints:

1 <= n <= 9
1 <= k <= n!
"""


class Solution:
    """
    Brute Force
    - find all permutation
    - sort them
    - get the kth permutation

    Optimal
    - for each number, calculate number of permutation possible
    - find the block in which kth permutation lies
    - do the same for all the numbers
    """
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        numbers = []
        for i in range(1, n):
            fact *= i
            numbers.append(i)
        numbers.append(n)
        ans = ""
        k -= 1
        while True:
            ans += str(numbers[k // fact])
            numbers.pop(k // fact)
            if not numbers:
                break
            k %= fact
            fact //= len(numbers)
        return ans
