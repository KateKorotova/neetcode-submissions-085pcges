# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None 
        # min_val = min(p.val, q.val)
        # max_val = max(p.val, q.val)
        # if min_val <= root.val <= max_val:
        #     return root
        # if root.val < min_val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # if root.val > min_val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # return root
        if p.val < node.val and q.val < node.val:
            return self.lowestCommonAncestor(node.left, p, q)
        elif p.val > node.val and q.val > node.val:
            return self.lowestCommonAncestor(node.right, p, q)
        else:
            return node
    
        return self.lowestCommonAncestor(node, p, q)
        