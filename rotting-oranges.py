class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        rotten = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]        
        minutes = 0

        while queue:
            r, c, time = queue.popleft()
            minutes = max(minutes, time)

            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    rotten += 1
                    queue.append((nr, nc, time + 1))
        
        return minutes if fresh == rotten else -1
