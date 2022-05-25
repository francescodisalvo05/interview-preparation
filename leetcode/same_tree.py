# 100 - https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# space = O(n) - if imbalanced | time = O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def recursion(m,n):
            if not m and not n: # both None 
                return True
            
            if not m or not n: # one of them is None
                return False
            
            if m.val != n.val: # they're not None but different
                return False
            
            if m.val == n.val: # they're equal
                return recursion(m.left,n.left) and recursion(m.right,n.right)
            
        return recursion(p,q)

# https://leetcode.com/problems/same-tree/solution/356238
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack = [(p,q)]
        
        while stack:
            (p,q) = stack.pop()
            if p and q and p.val == q.val:
                stack.extend([(p.left,q.left),(p.right,q.right)])
            elif p or q:
                return False
            
        return True