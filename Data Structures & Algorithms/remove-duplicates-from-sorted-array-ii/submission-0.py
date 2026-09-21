class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextOpen = 2
        toCheck = 2
        
        if len(nums) <= 2:
            return len(nums)
        
        while toCheck < len(nums):
            if nums[toCheck] != nums[nextOpen - 2]:
                nums[nextOpen] = nums[toCheck]
                nextOpen += 1
            toCheck += 1
        return nextOpen
                