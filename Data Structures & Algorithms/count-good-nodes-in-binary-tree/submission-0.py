# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 
        max_left = root.val
        max_right = root.val
        res = 1

        def dfs(node, max_v):
            nonlocal res
            if not node:
                return 
            if node.val >= max_v:
                max_v = node.val
                res += 1
            dfs(node.left, max_v)
            dfs(node.right, max_v)
        
        dfs(root.left, max_left)
        dfs(root.right, max_right)
        return res
