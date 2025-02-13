class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for edge in edges:
            adj[edge[1]].append(edge[0])
            adj[edge[0]].append(edge[1])

        visiting = set()
        print(adj)

        def dfs(parent, node):
            if node in visiting:
                return False
            
            visiting.add(node)

            edges = adj[node]
            for next_node in edges:
                if next_node == parent:
                    continue
                if not dfs(node, next_node):
                    return False
            
            return True
        
        res = dfs(-1, 0)
        if res and len(visiting) == n:
            return True
        return False
        