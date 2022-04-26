# 152 - https://leetcode.com/problems/maximum-product-subarray/

# space = O(1) | time = O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # expanding maxium subarray
        # keep track of maximum and minimum
        # edge case: negative values!
        
        max_product, previous_max, previous_min = float('-inf'), 1, 1
        
        for n in nums:
            
            curr_max = max(n, n * previous_max, n * previous_min)
            curr_min = min(n, n * previous_max, n * previous_min)
            
            max_product = max(curr_max, max_product)
            
            previous_max, previous_min = curr_max, curr_min
            
        return max_product
        