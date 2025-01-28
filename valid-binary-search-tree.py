# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def in_order(root):
            if not root:
                return None
            
            in_order(root.left)
            arr.append(root.val)
            in_order(root.right)
        
        in_order(root)
        
        for i in range(len(arr)):
            if i + 1 == len(arr):
                break
            if arr[i+1] <= arr[i]:
                return False
        return True
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       
        def is_valid(root, minimum, maximum):
            if root is None:
                return True
            
            if not (minimum < root.val < maximum):
                return False
            
            return True and is_valid(root.left, minimum, root.val) and is_valid(root.right, root.val, maximum)
        
        return is_valid(root, float('-inf'), float('inf'))
        