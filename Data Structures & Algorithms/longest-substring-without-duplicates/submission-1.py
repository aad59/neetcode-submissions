class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        maxLength = 1
        L = 0
        R = 1
        seen = set()
        seen.add(s[0])

        while R < len(s) and L <= R:
            if L == R or s[R] not in seen:
                if maxLength < R - L + 1:
                    maxLength = R - L + 1
                seen.add(s[R])
                R += 1
            else:
                seen.remove(s[L])
                L += 1
                
        return maxLength
