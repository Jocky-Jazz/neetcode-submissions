class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(', '{', '[']
        closes = [')', '}', ']']
        for b in s:
            if (stack and b in closes and stack[-1] in opens and opens.index(stack[-1]) == closes.index(b)):
                stack.pop()
            else:
                stack.append(b)
                print(stack)
        return len(stack) == 0