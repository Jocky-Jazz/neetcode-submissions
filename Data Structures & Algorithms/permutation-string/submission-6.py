class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s2) < len(s1)):
            return False
        string = deque([])
        s1count = Counter(s1)
        count = dict()
        for ch in s2:
            if (count == s1count):
                return True
            if (ch in s1):
                string += ch
                count[ch] = count.get(ch, 0)+1
                while(string and count[ch] > s1count[ch]):
                    count[string.popleft()] -= 1
            else:
                string.clear()
                count.clear()
            print(string)
        return count == s1count