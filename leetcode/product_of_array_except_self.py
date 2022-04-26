# 238 - https://leetcode.com/problems/product-of-array-except-self

# space = O(n) | time = O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # with the first pass we have the multiplication
        # with the previous numbers whereas with the second 
        # one we also gather the following ones
        
        cum_prod, result = 1, []
        for n in nums:
            result.append(cum_prod)
            cum_prod *= n
            
        cum_prod = 1
        for idx in range(len(nums)-1,-1,-1):
            result[idx] *= cum_prod
            cum_prod *= nums[idx]
            
        return result
            