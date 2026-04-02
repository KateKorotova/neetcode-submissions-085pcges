# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getValues(self, root, value_list):
        if not root:
            return
        self.getValues(root.left, value_list)
        value_list.append(root.val) 
        self.getValues(root.right, value_list)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        value_list = []
        self.getValues(root, value_list)
        return value_list[k-1]


        