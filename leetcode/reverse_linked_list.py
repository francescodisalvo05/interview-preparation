# 206 - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time = O(n) | space = O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        previous, current = None, head
        
        while current:
            
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            
        return previous
    
        
            
            
            