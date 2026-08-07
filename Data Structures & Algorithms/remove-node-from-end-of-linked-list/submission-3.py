# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        map_idx = {}
        curr = head
        idx = 0 
        while curr:
            map_idx[idx] = curr
            curr = curr.next 
            idx += 1
        count = len(map_idx)
        if count == n:
            return head.next
        prev = map_idx[count - n - 1]
        node = map_idx[count - n]
        prev.next = node.next
        return head
        