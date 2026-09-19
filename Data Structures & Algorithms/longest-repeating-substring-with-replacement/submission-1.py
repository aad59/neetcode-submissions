class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap = {s[0]: 1}
        L = 0
        R = 1
        maxLength = 1
        maxFreq = 1

        while R < len(s) and L <= R:
            if s[R] not in myMap:
                myMap[s[R]] = 0
            myMap[s[R]] += 1
            if myMap[s[R]] > maxFreq:
                maxFreq = myMap[s[R]]
            
            if R - L + 1 - maxFreq > k:
                myMap[s[L]] -= 1
                L += 1
                R += 1
            else:
                if R - L + 1 > maxLength:
                    maxLength = R - L + 1
                R += 1
        return maxLength