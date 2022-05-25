# 283 - https://leetcode.com/problems/move-zeroes/

# time = O(n) | space = O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        last_zero_idx = 0
        
        for idx in range(len(nums)):
            
            # when you encounter 0 it doesn't increment
            # therefore it will be the actual index of the 0
            
            if nums[idx] != 0:
                nums[last_zero_idx] = nums[idx]
                last_zero_idx += 1 
                
        for idx in range(last_zero_idx,len(nums)):
            nums[idx] = 0
            
        
            
            