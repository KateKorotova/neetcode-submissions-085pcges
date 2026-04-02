class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = set(['(', '{', '['])
        closed_brackets = set([')', '}', ']'])
        pairs = {')': '(', '}': '{', ']': '['}
        if len(s) < 2:
            return False
        for br in s:
            if br in open_brackets:
                stack.append(br)
            if br in closed_brackets:
                if not stack:
                    return False
                last_bracket = stack.pop()
                if pairs[br] != last_bracket:
                    return False
        return stack == []

