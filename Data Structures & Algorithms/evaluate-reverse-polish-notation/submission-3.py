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
                        if (a*b<0):
                            values.append(-(abs(b)//abs(a)))
                        else:
                            values.append(abs(b)//abs(a))
                    case '*':
                        values.append(b*a)
            else:
                values.append(int(n))
            print(values)
        return values[0]
