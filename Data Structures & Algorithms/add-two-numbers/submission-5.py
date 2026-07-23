# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one = 0
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            curr.next = ListNode()
            value = l1.val + l2.val + one
            digit = value % 10 
            one = value // 10

            curr.next.val = digit 
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        remaining = l1 if l1 else l2
        while remaining:
            curr.next = ListNode()
            value = remaining.val + one
            digit = value % 10 
            one = value // 10

            curr.next.val = digit

            curr = curr.next
            remaining = remaining.next
        if one >= 1:
            node = ListNode(1)
            curr.next = node
        return dummy.next
            