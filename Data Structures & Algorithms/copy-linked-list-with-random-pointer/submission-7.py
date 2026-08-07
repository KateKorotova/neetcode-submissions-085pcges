"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        hashMap = {}
        curr = head
        while curr:
            new_node = Node(curr.val)
            hashMap[curr] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            hashMap[curr].next = hashMap.get(curr.next, None)
            hashMap[curr].random = hashMap.get(curr.random, None)
            curr = curr.next

        return hashMap[head]