# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def DFS(node):
            if node is None:
                return
            temp = node.left
            node.left = node.right
            node.right = temp
            DFS(node.left)
            DFS(node.right)
        
        DFS(root)
        return root
        