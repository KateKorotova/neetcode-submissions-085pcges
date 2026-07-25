import operator

opt = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for token in tokens:
            if token in opt:
                b = int(res.pop())
                a = int(res.pop())
                val = int(opt[token](a, b))
                res.append(val)
            else:
                res.append(token)
        return int(res[-1])


        