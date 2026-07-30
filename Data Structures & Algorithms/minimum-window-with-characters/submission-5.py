class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(s)<len(t)):
            return ""
        tcount = Counter(t)
        j = 0
        res = ""
        i = 0
        while (j < len(s) and i < len(s)):
            while (i < len(s) and not max(tcount.values()) == 0):
                if (s[i] in tcount):
                    tcount[s[i]] -= 1
                i += 1
            while (j < len(s) and max(tcount.values()) == 0):
                if (s[j] in tcount):
                    tcount[s[j]] += 1
                j += 1
            tcount[s[j-1]] -= 1
            if (max(tcount.values()) == 0 and ((not res) or len(res) > i-j+1)):
                res = s[j-1:i]
            tcount[s[j-1]] += 1
        return res
                
            