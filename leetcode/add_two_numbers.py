# 2 - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# space = O(max(n,m)) | time = O(max(n,m))
# n,m are the length of l1 and l2, respectively
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # edge case 1 : different length
        # edge case 2 : finaly carry
        
        result = ListNode()
        current = result
        carry = 0
        
        while l1 or l2 or carry:
            
            curr_sum = (l1.val if l1 else 0) + \
                       (l2.val if l2 else 0) + \
                       carry # either 0 or 1
            
            current.next = ListNode(curr_sum % 10)
            carry = 1 if curr_sum > 9 else 0
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next