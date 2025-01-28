# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        def traverse(root, level):
            if not root:
                return None
            
            if len(res) == level:
                res.append([])
            
            res[level].append(root.val)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)
        
        traverse(root, 0)
        return res
    