class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        cache = [[-1 for _ in range(n)] for _ in range(m)]

        def helper(i, j):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            if i == m - 1 and j == n - 1:
                return 1
            
            cache[i][j] = helper(i + 1, j) + helper(i, j + 1)
            return cache[i][j]
        
        return helper(0, 0)