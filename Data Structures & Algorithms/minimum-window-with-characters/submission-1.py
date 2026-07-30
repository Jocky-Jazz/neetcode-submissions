class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(s)<len(t)):
            return ""
        tcount = Counter(t)
        f = False
        j = 0
        res = ""
        i = 0
        while (True):
            if (max(tcount.values()) == 0):
                if ((not res) or i-j < len(res)):
                    res = s[j:i]
                i = j+1
                f = False
                tcount = Counter(t)
            if (i == len(s)):
                return res
            if (s[i] in tcount):
                if (not f):
                    f = True
                    j = i
                tcount[s[i]] -= 1
            i += 1
            