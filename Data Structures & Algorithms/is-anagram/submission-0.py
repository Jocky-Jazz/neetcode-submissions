class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_new = sorted(s)
        t_new = sorted(t)
        return (s_new == t_new)