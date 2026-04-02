# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0 
        # if not root.left:
        #     return 1 + self.maxDepth(root.right)
        # if not root.right:
        #     return 1 + self.maxDepth(root.left)
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))     
        if not root:
            return 0 
        depth = 0
        stack = deque([root])
        while stack:
            stack_len = len(stack)
            for _ in range(stack_len):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            depth += 1
        return depth






