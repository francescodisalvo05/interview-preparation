# 338 - https://leetcode.com/problems/counting-bits/


# space = O(n) | time = O(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n+1)
        offset = 1 #MSB
        
        for idx in range(1, n+1):
            # update offset
            if offset * 2 == idx:
                offset = idx
                
            dp[idx] = 1 + dp[idx - offset]                
            
        return dp