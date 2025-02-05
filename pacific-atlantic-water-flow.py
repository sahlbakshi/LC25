class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # brute force way is to run bfs on each node 
        # keep going until we reach pacific or atlantic and mark it OR
        # reach a previous starting node we considered to be the oslution
        # or queue is empty

        prev = set()
        res = []
        rows, cols = len(heights), len(heights[0])

        def bfs(i, j):
            visited = set()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            queue = deque()
            queue.append((i, j))
            reached_atlantic = False
            reached_pacific = False

            while queue:
                r, c = queue.popleft()

                if (r, c) in prev:
                    return True
                
                if r == 0 or c == 0:
                    reached_pacific = True
                
                if r == rows - 1 or c == cols - 1:
                    reached_atlantic = True
                
                if reached_pacific and reached_atlantic:
                    return True

                for direction in directions:
                    nr = r + direction[0]
                    nc = c + direction[1]
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if heights[nr][nc] <= heights[r][c] and (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
            
            return reached_atlantic and reached_pacific

        for i in range(rows):
            for j in range(cols):
                if bfs(i, j):
                    res.append([i, j])
                    prev.add((i, j))

        return res


class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # smart way is to run bfs on all nodes left, top
        # these already touch the pacific ocean so check which node
        # next to it can go from that node to this node then 
        # it means that we can reach the node u came from
        # do this for the atlantic ocean as well
        # and then take the intersection of both sets

        atlantic = set()
        pacific = set()
        rows, cols = len(heights), len(heights[0])

        for i in range(rows):
            pacific.add((i, 0))
            atlantic.add((i, cols-1))
        
        for i in range(cols):
            pacific.add((0, i))
            atlantic.add((rows-1, i))

        def bfs(ocean):
            queue = deque()

            set_used = atlantic
            if ocean == 'pacific':
                set_used = pacific

            for i, j in set_used:
                queue.append((i, j))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited = set()

            while queue:
                r, c = queue.popleft()
                visited.add((r, c))

                for direction in directions:
                    nr = r + direction[0]
                    nc = c + direction[1]

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        queue.append((nr, nc))
                        set_used.add((nr, nc))
            
        bfs('atlantic')
        bfs('pacific')

        res = []
        res_set = atlantic.intersection(pacific)

        for r, c in res_set:
            res.append([r, c])

        return res
