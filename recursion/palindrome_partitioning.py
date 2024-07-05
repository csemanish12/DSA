"""

Topics
Companies
Given a string s, partition s such that every
substring
 of the partition is a
palindrome
. Return all possible palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters
"""
import copy
from typing import List


class Solution:
    """
    Partition at each index recursively
    """
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        self.__find_partitions(0, [], s, n, ans)

        return ans

    def __find_partitions(self, index, partitions, s, n, ans):
        if index == n:
            ans.append(copy.deepcopy(partitions))
            return

        for i in range(index, n):
            if self.__is_palindrome(s, index, i):
                partitions.append(s[index:i+1])
                self.__find_partitions(i+1, partitions, s, n, ans)
                partitions.pop()

    def __is_palindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True


s = Solution()

input_1 = "aab"
print("output 1:", s.partition(input_1))
