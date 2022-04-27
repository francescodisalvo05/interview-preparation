# 11 - https://leetcode.com/problems/container-with-most-water/

# space = O(1) | time = O(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        
        # two pointers
        left, right = 0, len(height)-1
        
        while left < right:
            
            b = right - left
            h = min(height[right],height[left])
            
            area = b * h
            
            max_area = max(area,max_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area