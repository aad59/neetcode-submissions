class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums[0:]
        prefix[0] = 1
        suffix = nums[0:]
        suffix[-1] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            j = len(nums) - 1 - i
            suffix[j] = suffix[j + 1] * nums[j + 1]
        
        ret = []
        for i in range(len(nums)):
            ret.append(prefix[i] * suffix[i])
        
        return ret