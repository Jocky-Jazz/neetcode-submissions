class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(s)<len(t)):
            return ""
        tcount = Counter(t)
        j = 0
        res = ""
        i = 0
        left = len(tcount)
        scount = dict()
        while (j < len(s) and i < len(s)):
            while (i < len(s) and left>0):
                if (s[i] in t):
                    scount[s[i]] = scount.get(s[i], 0)+1
                    if (scount[s[i]] == tcount[s[i]]):
                        left -= 1
                i += 1
            while (j < len(s) and left == 0):
                if (s[j] in t):
                    scount[s[j]] -= 1
                    if (scount[s[j]] < tcount[s[j]]):
                        left += 1
                j += 1
            if ((j or not left) and ((not res) or len(res) > i-j+1)):
                res = s[j-1:i]
        return res
                
            