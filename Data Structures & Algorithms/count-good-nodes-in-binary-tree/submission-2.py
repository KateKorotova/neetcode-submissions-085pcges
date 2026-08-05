# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_v):
            if not node:
                return 0
            res = 1 if node.val >= max_v else 0
            max_v = max(node.val, max_v)
                
            res += dfs(node.left, max_v)
            res += dfs(node.right, max_v)
            return res

        return dfs(root, root.val)
