# Optimal Neetcode solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max_profit = 0
        i = 0
        j = 1

        while j < len(prices):
            if prices[j] > prices[i]:
                max_profit = max(max_profit, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return max_profit        

# Optimized solution - fastest
# Time complexity: O(n)
# Space complexity: O(1)
    
'''
In this version, we iterate through the list of prices only once. For each price, we update our min_price and max_profit as necessary. This reduces the time complexity to O(n), where n is the number of prices.

We can also reduce the space complexity by using two variables instead of a list. This reduces the space complexity to O(1).
'''`
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit



# This works but is too slow
# Time complexity: O(n^2)
# Space complexity: O(1)

'''
The solution has a time complexity of O(n^2) because it uses two nested loops to compare all possible pairs of buy and sell prices. This can be optimized to O(n) by keeping track of the minimum price and the maximum profit at the same time.
'''
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max_profit = 0
        for buy_price in range(len(prices) - 1):
            for sale_price in range(buy_price + 1, len(prices)):
                profit = prices[sale_price] - prices[buy_price]
                max_profit = max(max_profit, profit)
        return max_profit
    

