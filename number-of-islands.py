class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited or grid[r][c] == '0':
                    continue

                visited.add((r, c))
                islands += 1

                queue = deque()
                queue.append((r, c))
                
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                while queue:
                    cr, cc = queue.popleft()

                    for direction in directions:
                        nr = cr + direction[0]
                        nc = cc + direction[1]

                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == '1' and (nr, nc) not in visited:
                                queue.append((nr, nc))
                                visited.add((nr, nc))
        
        return islands
