# 121 - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# space = O(1) | time = O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # keep track of the minimum price and 
        # update the current profit (its lower bound is 0)
        
        min_price, max_profit = float('inf'), 0
        
        for curr_price in prices:
            min_price = min(min_price,curr_price)
            max_profit = max(max_profit,curr_price - min_price)
        
        return max_profit


# brute force 
# space = O(1) | time = O(n^2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = float('-inf')
        
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                profit = max(profit,prices[j]-prices[i])
                
        return profit if profit > 0 else 0