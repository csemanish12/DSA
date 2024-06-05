"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    """
    using hashmap, keep char as key and its index as value.
    when finding repeating char in hashmap, move the left pointer to next index of last found.
    This will reduce the steps it takes for left pointer to reach as there was repeating character
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = right = 0
        n = len(s)
        char_map = {}
        while right < n:
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)

            char_map[s[right]] = right
            length = max(length, right - left + 1)
            right += 1

        return length


s = Solution()

input_1 = "abcabcbb"
print("output 1:", s.lengthOfLongestSubstring(input_1))

input_2 = "pwwkew"
print("output 1:", s.lengthOfLongestSubstring(input_1))

