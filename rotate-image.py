class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        arr = []

        rows = len(matrix)
        cols = len(matrix[0])

        for row in matrix:
            arr.append([])
        
        r = rows - 1
        while r >= 0:
            for c in range(cols):
                arr[c].append(matrix[r][c])
            r -= 1
        
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = arr[r][c]
 
     
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reflection
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
