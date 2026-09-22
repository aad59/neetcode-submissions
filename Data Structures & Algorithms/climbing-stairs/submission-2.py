class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0 for _ in range(n+1)]

        def climbHelper(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            if cache[n] != 0:
                return cache[n]
            
            cache[n] = climbHelper(n-1) + climbHelper(n-2)
            return cache[n]
        
        return climbHelper(n)