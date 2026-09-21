class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextOpen = 1
        toCheck = 1

        while toCheck < len(nums):
            if nums[toCheck] != nums[toCheck - 1]:
                nums[nextOpen] = nums[toCheck]
                nextOpen += 1
            toCheck += 1
        return nextOpen