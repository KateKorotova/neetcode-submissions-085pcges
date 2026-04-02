class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for br in s:
            if br in pairs:
                if stack and pairs[br] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(br)
        return stack == []

