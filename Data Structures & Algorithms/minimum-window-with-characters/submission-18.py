class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(s)<len(t)):
            return ""
        i, j, start, end = 0, 0, 0, 0
        tcount = Counter(t)
        left = len(tcount)
        scount = dict()
        while (j < len(s) and i < len(s)):
            while (i < len(s) and left>0):
                if (s[i] in t):
                    scount[s[i]] = scount.get(s[i], 0)+1
                    if (scount[s[i]] == tcount[s[i]]):
                        left -= 1
                i += 1
            #print(i, j, left)
            while (j < len(s) and left == 0):
                if (s[j] in t):
                    scount[s[j]] -= 1
                    if (scount[s[j]] < tcount[s[j]]):
                        left += 1
                j += 1
            #print(i, j, left)
            if ((left==1 and j>0) and (not(start or end) or end-start > i-j+1)):
                start, end = j-1, i
        return s[start:end]
                
            