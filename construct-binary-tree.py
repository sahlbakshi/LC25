# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode()

        def make_tree(preorder, inorder):
            if not preorder or not inorder:
                return None

            root = TreeNode(preorder[0])
            for i in range(len(inorder)):
                if inorder[i] == root.val:
                    break
            
            root.left = make_tree(preorder[1:1+i], inorder[:i])
            root.right = make_tree(preorder[1+i:], inorder[i+1:])
            return root
        
        return make_tree(preorder, inorder)
