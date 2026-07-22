class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = {'(':1, '{':2, '[':3}
        closes = {')':1, '}':2, ']':3}
        for b in s:
            if (stack and opens.get(stack[-1], -1) == closes.get(b, -2)):
                stack.pop()
            else:
                stack.append(b)
        return len(stack) == 0