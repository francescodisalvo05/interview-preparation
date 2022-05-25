# 234 - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time = O(n) | space = O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        stack, fast, slow = [], head, head
        
        # put the slow pointer in the middle
        while fast and fast.next:
            # store the left hand side
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        # edge case: odd length - skip
        if fast:
            slow = slow.next
            
        while slow:
            if slow.val != stack.pop():
                return False
            
            slow = slow.next
            
        return True
            
        
        
# inspiration from https://leetcode.com/problems/palindrome-linked-list/discuss/2056426/Python-oror-faster-99.38-oror-memory-95.51
# reverse slow pointer

# space = O(1) |  time = O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast = slow = head
        slow_prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            # reverse slow
            slow.next, slow_prev, slow = slow_prev, slow, slow.next
        
        # edge case - odd length
        right = slow.next if fast else slow
        left = slow_prev
       
        while left:
            if left.val != right.val:
                return False
            # shift
            left = left.next
            right = right.next
            
        return True

        
        
        
            