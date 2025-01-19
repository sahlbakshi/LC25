# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def DFS(node, minimum, maximum):
            if not node:
                return True
            
            if not (minimum < node.val < maximum):
                return False
            
            return True and DFS(node.left, minimum, node.val) and DFS(node.right, node.val, maximum)
        
        return DFS(root, float('-inf'), float('inf'))
                