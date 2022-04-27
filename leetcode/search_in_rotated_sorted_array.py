
# 33 - https://leetcode.com/problems/search-in-rotated-sorted-array/

# space = O(1) | time = O(logn)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # updated dicotomic search
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left, right = 0, len(nums) - 1

        while left <= right:

            m = left + (right - left) //2

            if nums[m] == target:
                return m

            if nums[left] <= nums[m]:
                # [left..m] is sorted 
                if nums[left] <= target and target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            else:
                # [m..right] is sorted
                if target <= nums[right] and target > nums[m]:
                    left = m + 1
                else:
                    right = m - 1

        return -1