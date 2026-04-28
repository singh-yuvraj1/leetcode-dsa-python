# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


#----------------------------------Brute Force Solution----------------------------------
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit
if __name__== "__main__":
    a = Solution()
    prices1 = [7,1,5,3,6,4]
    print(a.maxProfit(prices1))  # 5

    prices2 = [7,6,4,3,1]
    print(a.maxProfit(prices2))  # 0    
## Time Complexity: O(n^2) where n is the length of the input array. We have two nested loops that iterate through the array to calculate the profit for each pair of days.
## Space Complexity: O(1) since we are not using any additional data structures that grow with the input size.


