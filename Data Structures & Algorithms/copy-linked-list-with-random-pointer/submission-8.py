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
        hashMap = defaultdict(lambda: Node(0))
        hashMap[None] = None
        cur = head
        while cur:
            hashMap[cur].val = cur.val
            hashMap[cur].next = hashMap[cur.next]
            hashMap[cur].random = hashMap[cur.random]
            cur = cur.next
        return hashMap[head]
    