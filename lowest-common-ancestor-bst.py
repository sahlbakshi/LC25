# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minimum = min(p.val, q.val)
        maximum = max(p.val, q.val)

        if not root:
            return None
        
        if minimum <= root.val <= maximum:
            return root
        
        if root.val > minimum and root.val > maximum:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

        