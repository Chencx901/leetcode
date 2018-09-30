# Say you have an array for which the ith element 
# is the price of a given stock on day i.
# If you were only permitted to complete as many transactions as you like 
# (i.e., buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), 
# profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit += (prices[i]-buy)
                buy = prices[i]
        return profit