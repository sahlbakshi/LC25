# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        prev = [None] 

        def dfs(node):
            if not node:
                return None
            
            dfs(node.right)
            dfs(node.left)

            node.right = prev[0]
            node.left = None
            prev[0] = node

        """
        def dfs(node):
            if not node:
                return None
            
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            if node.left:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            
            return right_tail or left_tail or node
        """
        
        dfs(root)
