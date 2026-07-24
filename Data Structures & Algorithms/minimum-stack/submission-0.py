class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        curr_min = self.minStack[-1] if self.minStack else float('inf')
        new_min = curr_min if curr_min <= val else val
        self.minStack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return []
        
    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return [] 
