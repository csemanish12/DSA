"""
Problem Statement: You are given an array. The task is to reverse the array and print it.

Examples
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

"""
class Solution:
    def reverseArray(self, arr):
        # code here
        self._reverseArray(arr, 0, len(arr))
    
    def _reverseArray(self, arr, index, n):
        if index == n // 2:
            return
        arr[index], arr[n-index-1] = arr[n-index-1], arr[index]
        self._reverseArray(arr, index+1, n)
        

input_1 = [1,2,3,4,5]
Solution().reverseArray(input_1)
print("reverse is:", input_1)

input_2 = [1,2,3,4]
Solution().reverseArray(input_2)
print("reverse is:", input_2)

"""
Time complexity: O(n/2)
- we recursively call till n/2

Space complexity: O(n/2)
- we recursively call  till n/2 and hence n/2 stack space is used
"""