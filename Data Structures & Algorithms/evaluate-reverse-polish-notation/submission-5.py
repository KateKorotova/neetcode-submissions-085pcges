import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # Define the mapping dictionary
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for token in tokens:
            if token in ops:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                curr_res = ops[token](val2, val1)
                stack.append(curr_res)
            else:
                stack.append(token)
        return int(stack.pop())
        