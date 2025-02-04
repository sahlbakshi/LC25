from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        hashmap = {}

        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            
            clone_node = Node(node.val, [])
            hashmap[node] = clone_node

            for neighbor in node.neighbors:
                clone_neighbor = dfs(neighbor)
                hashmap[node].neighbors.append(clone_neighbor)
            
            return clone_node
        
        return dfs(node)
