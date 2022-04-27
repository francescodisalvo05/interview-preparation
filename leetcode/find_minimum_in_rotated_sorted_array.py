# 153 - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# space = O(1) | time = O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # 1. Find pivot
        # 2. Apply dicotomic search
        
        N = len(nums)
        
        # edge case #1 - just one element
        if N == 1:
            return nums[0]
        
        # edge case #2 - no rotation
        if nums[0] <= nums[N-1]:
            return nums[0]
        
        
        # apply binary search
        left, right = 0, N - 1
        
        while left <= right:
            
            m = left + (right - left) // 2
            
            # m+1 is the "max/min" swap (i.e. pivot)
            if nums[m] > nums[m+1]:
                return nums[m+1]
            # m is the "max/min" swap (i.e. pivot)
            if nums[m-1] > nums[m]:
                return nums[m]
            
            # no solution anymore, update pointers
            if nums[m] > nums[0]:
                left = m + 1
            else:
                right = m - 1
        
        