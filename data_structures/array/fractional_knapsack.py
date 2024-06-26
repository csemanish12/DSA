"""
Given weights and values of n items, we need to put these items in a knapsack of capacity w to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item here.

Example 1:

Input:
n = 3
w = 50
value[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.000000
Explanation:
Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80, so the total value becomes 60+100+80.0=240.0
Thus, total maximum value of item we can have is 240.00 from the given capacity of sack.
Example 2:

Input:
n = 2
w = 50
value[] = {60,100}
weight[] = {10,20}
Output:
160.000000
Explanation:
Take both the items completely, without breaking.
Total maximum value of item we can have is 160.00 from the given capacity of sack.
Your Task :
Complete the function fractionalKnapsack() that receives maximum capacity w, an array of structure/class, and size n and returns a double value representing the maximum value in knapsack.
Note: The details of structure/class is defined in the comments above the given function.

Expected Time Complexity : O(NlogN)
Expected Auxilliary Space: O(1)

Constraints:
1 <= n <= 105
1 <= w <= 109
1 <= valuei, weighti <= 104


"""


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    """
    sort the items by value/weight in descending order
    """
    def fractionalknapsack(self, w, arr, n):
        arr = sorted(arr, key=lambda x: -(x.value / x.weight))

        occupied = 0
        value = float(0)
        for i in range(n):
            if occupied == w:
                break

            if arr[i].weight + occupied <= w:
                occupied += arr[i].weight
                value += arr[i].value
            else:
                remaining = w - occupied
                val = (arr[i].value / arr[i].weight) * remaining
                occupied += remaining
                value += val

        return value
