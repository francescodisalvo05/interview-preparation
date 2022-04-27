# 15 - https://leetcode.com/problems/3sum/

# space = O(n) | time = O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = set() # avoid duplicates 
        nums.sort() # take advantage of the position
        seen = set() # keep track of the already seen solutions
        
        for i in range(len(nums)):
            
            # duplicates
            if i > 2 and nums[i] == nums[i-2]:
                continue
                
            for j in range(i+1,len(nums)):
                curr_sum = -(nums[i]+nums[j])
                if curr_sum in seen:
                    result.add((nums[i],nums[j],curr_sum))
                    
            seen.add(nums[i]) # check only "i" because "j" is just as slider
            
        return result
        


# space = O(n) | time = O(n^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
    
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):

                    if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:   
                        
                        # avoid duplicates
                        sorted_list = sorted([nums[i], nums[j], nums[k]])
                        
                        if sorted_list not in output:
                            output.append(sorted_list)
                            
        return output