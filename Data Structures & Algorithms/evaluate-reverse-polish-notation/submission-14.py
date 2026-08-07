import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opt = {
            '+': operator.add,
            '-': operator.sub ,
            '*': operator.mul,
            '/': operator.truediv
        }
        stack = []
        for token in tokens:
            if token in opt:
                b = stack.pop()
                a = stack.pop()
                val = int(opt[token](a, b))
                stack.append(val)
            else:
                stack.append(int(token))
        return stack[-1]