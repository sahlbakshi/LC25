"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        nodes = []
        
        def dfs(node, level):
            if not node:
                return 0
            
            if len(nodes) == level:
                nodes.append([])
            
            nodes[level].append(node)
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        
        for i in range(len(nodes)):
            for j in range(len(nodes[i])):
                if j + 1 == len(nodes[i]):
                    nodes[i][j].next = None
                else:
                    nodes[i][j].next = nodes[i][j+1]
        
        return root
        """

        if not root:
            return root
        
        leftmost = root

        while leftmost.left:

            current = leftmost

            while current:

                current.left.next = current.right

                if current.next:
                    current.right.next = current.next.left
                
                current = current.next
        
            leftmost = leftmost.left
        
        return root
