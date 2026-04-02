# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, low, high):
        if not root:
            return True
        if not (low < root.val < high) :
            return False
        left_tree = self.helper(root.left, low, root.val)
        right_tree = self.helper(root.right, root.val, high)
        return left_tree and right_tree


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        high = float('inf')
        low = float('-inf')
        return self.helper(root, low, high)


