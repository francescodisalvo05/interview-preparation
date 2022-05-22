# 876 - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# fast and slow pointer - from the solution: 
# When traversing the list with a pointer slow, 
# make another pointer fast that traverses twice as fast. 
# When fast reaches the end of the list, slow must be in the middle.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow


# brute force
# space = O(n) | time = O(n)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node_list = []

        while head:
            node_list.append(head)
            head = head.next
            
        return node_list[len(node_list) // 2]



# brute force
# space = O(1) | time = O(n)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # brute force
        dummy, result, counter = head, head, 0
        
        while dummy:
            counter += 1
            dummy = dummy.next
            
        middle = int(counter/2)
        
        for _ in range(middle):
            result = result.next
            
        return result
        