"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node, clone_map={}):
        if node in clone_map:
            return clone_map[node]
        clone_node = Node(node.val)
        clone_map[node] = clone_node

        for neighbor in node.neighbors:
            clone_neighbor = self.dfs(neighbor, clone_map)
            clone_node.neighbors.append(clone_neighbor)
        return clone_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 
        return self.dfs(node)