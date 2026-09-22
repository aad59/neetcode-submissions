class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def helper(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = max(nums[i] + helper(i + 2), helper(i + 1))
            return cache[i]
        return helper(0)