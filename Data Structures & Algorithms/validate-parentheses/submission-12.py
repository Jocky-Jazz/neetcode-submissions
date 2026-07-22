class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        for b in s:
            if b in mapping:
                if (stack and mapping.get(b, -1) == stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return not stack