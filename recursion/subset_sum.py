"""
Given a list arr of n integers, return sums of all subsets in it. Output sums can be printed in any order.



Example 1:

Input:
n = 2
arr[] = {2, 3}
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then
Sum = 2+3 = 5.
Example 2:

Input:
n = 3
arr = {5, 2, 1}
Output:
0 1 2 3 5 6 7 8
Your Task:
You don't need to read input or print anything. Your task is to complete the function subsetSums() which takes a list/vector and an integer n as an input parameter and returns the list/vector of all the subset sums.

Expected Time Complexity: O(2n)
Expected Auxiliary Space: O(2n)

Constraints:
1 <= n <= 15
0 <= arr[i] <= 104


"""


class Solution:
    """
    1. number of subsets that can be formed for an array with n element = 2^n
    eg: n = 3
        number of subset = 2^3 = 8

    Approach 1: Brute Force
    1. Generate power set
    2. Find the sum of each subset
    Time = 0 (2^N * N)
    Space  = O (2*N)

    Approach 2: Optimal
    1. Use Recursion to pick and not pick for each index. Each subset can be formed by picking and not picking
    elements at specific indexes.
    eg: say we have an array [3,1,2].
    One of the subset is [3,2], we can obtain this subset by picking index 0 and 2 and not picking index 1.
    We can do the same for remaining subsets

    Time = 0 (2^N)  -> each index has 2 ways, and there can be n indexes.
    Space = 0 (2^N) -> numer of subsets that can be generated. we store sum for each subset.
    """

    def subsetSums(self, arr, n):
        # code here
        subset_sum = []
        self.subset_sum(0, 0, arr, n, subset_sum)

        return subset_sum

    def subset_sum(self, index, sum, arr, n, subset_sum):
        if index == n:
            subset_sum.append(sum)
            return

        # pick
        self.subset_sum(index + 1, sum + arr[index], arr, n, subset_sum)

        # not pick
        self.subset_sum(index + 1, sum, arr, n, subset_sum)