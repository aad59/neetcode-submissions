class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        window = 0
        total = 0
        
        for R in range(k):
            window += arr[R]
        if window >= threshold:
            total += 1

        for R in range(k, len(arr)):
            window += arr[R]
            window -= arr[R-k]
            if window >= threshold:
                total += 1
        return total