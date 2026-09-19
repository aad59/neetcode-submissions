class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        globalMax = nums[0]
        currMin = 0
        globalMin = nums[0]

        total = 0

        for i in range(len(nums)):
            currMax = max(currMax + nums[i], nums[i])
            currMin = min(currMin + nums[i], nums[i])
            
            total += nums[i]

            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)

        return max(globalMax, total-globalMin) if globalMax > 0 else globalMax