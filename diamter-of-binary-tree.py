# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        largest_diameter = [0]

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = left + right

            largest_diameter[0] = max(largest_diameter[0], diameter)
            
            return 1 + max(left, right)

        dfs(root)
        return largest_diameter[0]
