# 704 - https://leetcode.com/problems/binary-search/

# space = O(1) | time = O(logn)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def recursion(start,end,target):
            
            if start > end:
                return -1
            
            m = (start + end) // 2
            
            if nums[m] == target:
                return m
            
            elif nums[m] > target:
                return recursion(start,m-1,target)
            else:
                return recursion(m+1,end,target)
            
            
        return recursion(0,len(nums)-1,target)