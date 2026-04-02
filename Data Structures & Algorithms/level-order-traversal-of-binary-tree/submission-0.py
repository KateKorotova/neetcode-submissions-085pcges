# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 
        stack = deque([root])
        result = []
        while stack:
            stack_len = len(stack)
            temp = []
            for _ in range(stack_len):
                node = stack.popleft()
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            result.append(temp)
           
        return result