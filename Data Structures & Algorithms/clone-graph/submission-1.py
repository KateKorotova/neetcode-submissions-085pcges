"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def clone(node):
            if node in hashMap:
                return hashMap[node]
            new_node = Node(node.val)
            hashMap[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(clone(neighbor))
            return new_node
        
        if not node:
            return None
        hashMap = {}
        return clone(node)