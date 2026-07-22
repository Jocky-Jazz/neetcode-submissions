class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for c in t:
            if (c in s):
                s = s.replace(c, "", 1)
            else:
                return False
        return True