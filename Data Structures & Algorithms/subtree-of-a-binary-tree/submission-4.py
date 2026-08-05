# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(q, p):
            if not q and not p:
                return True
            if (not q and p) or (q and not p):
                return False
            if p.val != q.val:
                return False
            left = isSameTree(q.left, p.left)
            right = isSameTree(q.right, p.right)
            return left and right 

        queue = deque([root])
        sameTree = False
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val and isSameTree(node, subRoot):
                sameTree = True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return sameTree



