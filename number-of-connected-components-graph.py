class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {}
        visit = set()

        for i in range(n):
            adj[i] = []

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        def dfs(node):
            if node in visit:
                return False

            visit.add(node)
            
            neighbours = adj[node]
            for neighbour in neighbours:
                if not dfs(neighbour):
                    return False
            return True

        components_count = 0
        for i in range(n):
            if i not in visit:
                components_count += 1
                dfs(i)
        
        return components_count
