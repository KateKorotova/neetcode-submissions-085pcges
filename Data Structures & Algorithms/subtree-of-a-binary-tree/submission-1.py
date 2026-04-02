# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSameTree(self, p, q):
        if not p and not q:
            return True 
        if (not p and q) or (not q and p):
            return False
        if p.val != q.val:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        result = False
        if not root:
            return False
        if root.val == subRoot.val:
            result = self.isSameTree(root, subRoot)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right or result

        