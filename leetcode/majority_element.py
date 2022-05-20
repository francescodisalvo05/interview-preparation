# 169 - https://leetcode.com/problems/majority-element/

# time = O(n) | space = O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashMap, N = defaultdict(int), len(nums)
        
        bound = floor(N/2)
        
        for n in nums:
            hashMap[n] += 1
            
            if hashMap[n] >= bound:
                return n
            
# time = O(nlogn) | space = O(1)        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        
        max_count, curr_count, bound = 0, 1, floor(len(nums)/2)
        
        for idx in range(1,len(nums)):
            if nums[idx-1] == nums[idx]:
                curr_count += 1
                if curr_count >= bound:
                    return nums[idx]
            else:
                curr_count = 1
                
        return 


# time = O(nlogn) | space = O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[floor(len(nums)/2)]
            
            
            
        