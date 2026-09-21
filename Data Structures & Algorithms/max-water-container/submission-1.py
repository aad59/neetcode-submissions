class Solution:
    def maxArea(self, heights: List[int]) -> int:
        myMax = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            if heights[L] <= heights[R]:
                myMax = max(myMax, heights[L] * (R - L))
                L += 1
            else:
                myMax = max(myMax, heights[R] * (R - L))
                R -= 1
        return myMax