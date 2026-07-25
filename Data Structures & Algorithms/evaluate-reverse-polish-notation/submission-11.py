import operator

opt = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv
}

class Solution:
    def rec(self, tokens):
        token = tokens.pop()
        if token in opt:
            b = self.rec(tokens)
            a = self.rec(tokens)
            val = opt[token](a, b)
            return int(val)
        else:
            return int(token)

    def evalRPN(self, tokens: List[str]) -> int:
        return self.rec(tokens)



        