class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s2) < len(s1)):
            return False
        s1count = Counter(s1)
        i = 0
        for i in range(len(s2) - len(s1) + 1):
            s2count = Counter(s2[i:i+len(s1)])
            if (s1count == s2count):
                return True
        return False