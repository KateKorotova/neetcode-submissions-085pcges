import operator

class Solution:
    def dfs(self, tokens):
        opt = {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                '/': operator.truediv
            }
        token = tokens.pop()
        if  token in opt:
            right = self.dfs(tokens)
            left = self.dfs(tokens)
            return int(opt[token](left, right))
        else:
            return int(token)

        
    def evalRPN(self, tokens: List[str]) -> int:
        return self.dfs(tokens)
        