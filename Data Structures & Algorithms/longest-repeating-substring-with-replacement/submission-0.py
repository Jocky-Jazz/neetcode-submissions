class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        string = deque([])
        maxlen = 0
        for ch in s:
            string.append(ch)
            count[ch] = count.get(ch, 0) + 1
            while (len(string) - max(count.values()) > k):
                count[string[0]] -= 1
                string.popleft()
            maxlen=max(maxlen, len(string))
        return maxlen
            