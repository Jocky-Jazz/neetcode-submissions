class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        maxlen = 0
        for ch in s:
            string = string[string.find(ch)+1:] + ch
            maxlen= max(len(string), maxlen)
        return maxlen