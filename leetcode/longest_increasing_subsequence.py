# 300 - https://leetcode.com/problems/longest-increasing-subsequence/

# time = O(n^2) | space = O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        N = len(nums)
        dp = [1] * N
            
        # start from the beginning
        for i in range(N-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i],1 + dp[j])
        
        return max(dp)