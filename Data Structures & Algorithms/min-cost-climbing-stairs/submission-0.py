class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1 for _ in range(len(cost))]

        def helper(i):
            if i >= len(cost):
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = min(cost[i] + helper(i + 1), cost[i] + helper(i + 2))
            return cache[i]
        
        return min(helper(0), helper(1))