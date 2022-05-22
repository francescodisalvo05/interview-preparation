# 543 - https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time = O(n) | space = O(1)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # store maximum diameter anytime
        self.result = 0
        
        def dfs(root):
            
            if not root:
                return 0

            left, right = dfs(root.left), dfs(root.right)

            self.result = max((left + right), self.result)

            return 1 + max(left, right)
        
        # scan each node
        dfs(root) 
        
        return self.result