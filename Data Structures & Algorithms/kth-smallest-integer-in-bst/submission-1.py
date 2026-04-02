# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, node, value_list):
        if not node:
            return
        self.helper(node.left, value_list)
        value_list.append(node.val)
        self.helper(node.right, value_list)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        value_list = []
        self.helper(root, value_list)
        return value_list[k-1]



        