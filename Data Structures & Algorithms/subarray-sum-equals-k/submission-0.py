class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix = 0
        prefix_log = {0:1}
        for num in nums:
            prefix += num
            diff = prefix - k
            if diff in prefix_log:
                total += prefix_log[diff]
            if prefix not in prefix_log:
                prefix_log[prefix] = 0
            prefix_log[prefix]  += 1
        return total