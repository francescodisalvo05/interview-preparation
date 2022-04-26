# 1 - https://leetcode.com/problems/two-sum/

# space = O(1) | time = O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}
        
        for idx,n in enumerate(nums):
            
            if n in hashMap.keys():
                return [hashMap[n],idx]
            
            hashMap[target-n] = idx
            
            
            