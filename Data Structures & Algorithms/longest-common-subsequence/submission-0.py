class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        cache = [[-1 for _ in range(n)] for _ in range(m)]

        def helper(i, j):
            if i >= m or j >= n:
                return 0
            
            if cache[i][j] != -1:
                return cache[i][j]
            
            if text1[i] == text2[j]:
                cache[i][j] = 1 + helper(i + 1, j + 1)
            else:
                cache[i][j] = max(helper(i + 1, j), helper(i, j + 1))
            return cache[i][j]
        return helper(0, 0)
        