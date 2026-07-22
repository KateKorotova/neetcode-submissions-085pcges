"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hashset = {}

        curr = head 
        while curr:
            hashset[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            # if curr.random:
            hashset[curr].next = hashset.get(curr.next, None)
            hashset[curr].random = hashset.get(curr.random, None)
            curr = curr.next

        return hashset[head]

