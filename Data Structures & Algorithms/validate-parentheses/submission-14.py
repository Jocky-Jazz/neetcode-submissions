class Solution:
    mapping = {')':'(', '}':'{', ']':'['}
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in Solution.mapping:
                if (stack and Solution.mapping[b] == stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return not stack