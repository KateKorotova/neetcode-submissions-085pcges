class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = [-1]
        for el in range(len(arr)-1, 0, -1):
            if arr[el] > stack[-1]:
                stack.append(arr[el])
            else:
                stack.append(stack[-1])
        return stack[::-1]
        