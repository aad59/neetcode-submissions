class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = nums[0:]
        suffix = nums[0:]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
            j = len(nums) - i - 1
            suffix[j] = suffix[j + 1] + suffix[j]
        
        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
        return -1
