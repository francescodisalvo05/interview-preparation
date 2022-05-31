# 141 - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# space = O(n) | time = O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                return True
            
        return False