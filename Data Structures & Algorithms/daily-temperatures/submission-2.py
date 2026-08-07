class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            if stack and stack[-1][0] < temp:
                while stack and stack[-1][0] < temp: 
                    t, i = stack.pop()
                    res[i] = idx - i 
            stack.append((temp, idx))
        return res