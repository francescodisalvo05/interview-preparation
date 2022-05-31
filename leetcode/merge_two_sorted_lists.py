# 21 - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# space = O(n+m) | time = O(max(m,n))
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        output = ListNode(0)
        dummy = output
        
        while list1 and list2:
            
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
                
            dummy = dummy.next
            
        dummy.next = list1 if list1 else list2
            
        return output.next