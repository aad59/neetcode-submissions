class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = len(nums) + 1
        L = 0
        R = 0
        currTotal = nums[0]

        while R < len(nums):
            if currTotal >= target:
                if R - L + 1 == 1:
                    return 1
                if R - L + 1 < minLength:
                    minLength = R - L + 1
                currTotal -= nums[L]
                L += 1
            else:
                R += 1
                if R < len(nums):
                    currTotal += nums[R]
        
        return minLength if minLength != len(nums) + 1 else 0
