"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import List

class Solution:
    """
    if you are selling on ith day, then you are buying on min price from 1st to i-1.
    We don't want loss, so initial profit will be 0.
    We will start from 1st index and iterate the entire list.
    While iterating, we will keep track of min price and profit. if profile is greater, than initially defined
    we keep the profile. If the current element is less than our initial min, we keep this min
    """
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            cost = prices[i] - min
            profit = max(cost, profit)
            min_price = min(min_price, prices[i])

        return profit
