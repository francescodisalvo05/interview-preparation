# 19 - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# space = O(n) | time = O(n)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        left = right = head
        
        # shift n times 
        for _ in range(n):
            right = right.next

        # if right is none it means it is the last node 
        # hence, the first from the left
        if not right:
            return head.next

        # shift both
        while right.next:
            left = left.next
            right = right.next

        # now the left node will point on the 
        # node that we need to skip
        left.next = left.next.next

        return head
        
        
        