class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        s = s.lower()

        while L <= R:
            if not s[L].isalnum():
                L+= 1
            elif not s[R].isalnum():
                R -= 1
            elif s[L] != s[R]:
                return False
            else:
                L+= 1
                R -= 1
        return True