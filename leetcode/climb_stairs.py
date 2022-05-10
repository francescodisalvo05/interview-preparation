# 70 - https://leetcode.com/problems/climbing-stairs/

# Nice explanations:
# - https://leetcode.com/problems/climbing-stairs/discuss/1792723/Python-or-In-Depth-Walkthrough-%2B-Explanation-or-DP-Top-Down-%2B-Bottom-Up
# - NeetCode : https://www.youtube.com/watch?v=Y0lT9Fck7qI

# space = O(1) | time = O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        
        # edge case -> save time
        if n == 1 or n == 2:
            return n
        
        dp = [-1] * (n + 1)  
        
        dp[1], dp[2] = 1, 2
        
        for idx in range(3, n + 1):
            dp[idx] = dp[idx - 1] + dp[idx - 2]
        
        return dp[n]
    