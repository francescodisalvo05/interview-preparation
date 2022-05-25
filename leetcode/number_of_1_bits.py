# 192 - https://leetcode.com/problems/number-of-1-bits/


# space = O(1) | time = O(logn)
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        
        while n > 0:
            if n & 1:
                count += 1
            n >>= 1
            
        return count

# "cheat"
# space = O(1) | time = O(n)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count("1")