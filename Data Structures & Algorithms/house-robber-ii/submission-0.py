class Solution:
    def rob(self, nums: List[int]) -> int:
        cache1 = [-1 for _ in range(len(nums))]
        cache2 = [-1 for _ in range(len(nums))]

        if len(nums) == 1:
            return nums[0]

        def helper(arr, myCache, i):
            if i >= len(arr):
                return 0
            if myCache[i] != -1:
                return myCache[i]            

            x = arr[i] + helper(arr, myCache, i + 2)
            y = helper(arr, myCache, i + 1)

            myCache[i] = max(x, y)
            return myCache[i]
        
        return max(helper(nums[:-1], cache1, 0), helper(nums[1:], cache2, 0)) 
