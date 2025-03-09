# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        prev = [None]
        first = middle = last = None

        def dfs(node):
            nonlocal first, middle, last 

            if not node:
                return
            
            dfs(node.left)

            if prev[0] and prev[0].val > node.val:
                if first is None:
                    first = prev[0]
                    middle = node
                else:
                    last = node

            prev[0] = node
            dfs(node.right)

        dfs(root)

        if last:
            first.val, last.val = last.val, first.val
        else:
            first.val, middle.val = middle.val, first.val
