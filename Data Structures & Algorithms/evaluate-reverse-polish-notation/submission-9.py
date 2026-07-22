class Solution:
    validops = {'+', '-', '*', '/'}
    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        for n in tokens:
            if (n in Solution.validops):
                a = values.pop()
                b = values.pop()
                match n:
                    case '+':
                        values.append(b+a)
                    case '-':
                        values.append(b-a)
                    case '/':
                        values.append(int(b/a))
                    case '*':
                        values.append(b*a)
            else:
                values.append(int(n))
        return values[0]
