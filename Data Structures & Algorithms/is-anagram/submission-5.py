class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            if (count.get(c, -1) == -1):
                return False
            else:
                count[c] = count[c] - 1
        for k in count:
            if (count[k] > 0):
                return False
        return True