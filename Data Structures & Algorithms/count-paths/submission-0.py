class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0 for _ in range(n)] for _ in range(m)]

        def memoization(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            
            if cache[i][j] != 0:
                return cache[i][j]
            
            cache[i][j] = memoization(i + 1, j) + memoization(i, j + 1)
            return cache[i][j]
        
        return memoization(0, 0)