class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = []
        zero_cols = []

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_rows.append(row)
                    zero_cols.append(col)
        
        for row in zero_rows:
            for col in range(cols):
                matrix[row][col] = 0
        
        for col in zero_cols:
            for row in range(rows):
                matrix[row][col] = 0
        