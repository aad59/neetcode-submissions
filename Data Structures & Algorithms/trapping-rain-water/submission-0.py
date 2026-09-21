class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = [0 for x in range(len(height))]
        myMax = 0
        for h in height:
            myMax = max(myMax, h)
            prefix.append(myMax)
        myMax = 0
        for i in range(len(height)):
            myMax = max(myMax, height[len(height) - 1 -i])
            suffix[len(height) - 1 - i] = myMax

        total = 0

        for i in range(len(height)):
            total += min(prefix[i], suffix[i]) - height[i] 
        return total