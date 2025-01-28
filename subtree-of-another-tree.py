# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same_tree(p, q):
            if not p and not q:
                return True

            if p and not q:
                return False
            
            if q and not p:
                return False
            
            if p.val != q.val:
                return False
            
            return True and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        if not subRoot:
            return True
        
        if not root:
            return False
        
        curr = is_same_tree(root, subRoot)
        return curr or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
