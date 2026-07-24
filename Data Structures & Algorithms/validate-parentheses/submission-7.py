class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}':'{', ']':'['}
        for el in s:
            if el in pairs:
                if len(stack) < 1:
                    return False
                last = stack.pop()
                if pairs[el] != last:
                    return False
            else:
                stack.append(el)
        return len(stack) == 0
