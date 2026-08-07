class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_el = val
        if self.stack:
            min_el = min(self.stack[-1][1], val)
        self.stack.append((val, min_el))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None
        
