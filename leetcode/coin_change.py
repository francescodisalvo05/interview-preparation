# 322 - https://leetcode.com/problems/coin-change/

# space = O(n) | time = O(n^2)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # amount + 1 is the "maximum" (initialize)
        dp = [amount + 1] * (amount + 1)
        # base case
        dp[0] = 0 
        
        for v in range(1,amount + 1):
            for c in coins:
                if v - c >= 0:
                    # it can be possible, so update
                    dp[v] = min(dp[v],1 + dp[v - c])
                    
                    
        return dp[amount] if dp[amount] != amount + 1 else -1
        
        
        