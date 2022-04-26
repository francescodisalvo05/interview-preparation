# 53 - https://leetcode.com/problems/maximum-subarray/

# space = O(1) | time = O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum, curr_sum = float('-inf'), 0
        
        for n in nums:
            
            # edge case : negative values
            curr_sum = max(curr_sum+n,n)
            max_sum = max(max_sum,curr_sum)
            
        return max_sum
            
            