# 217 - https://leetcode.com/problems/contains-duplicate/

# space = O(1) | time = O(n)
# 466ms | 25.9MB
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashMap = {}

        for n in nums:
            if n in hashMap.keys():
                return True
            hashMap[n] = 0
        
        return False


# space = O(1) | time = O(n)
# 486ms | 26MB
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


# space = O(1) | time = O(nlogn + n) = O(nlogn)
# 583ms | 26MB
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        
        for idx in range(1,len(nums)):
            if nums[idx] == nums[idx-1]:
                return True
            
        return False