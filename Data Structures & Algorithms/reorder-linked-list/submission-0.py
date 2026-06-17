# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev_val = {}
        prev = None 
        curr = head
        n = 0
        while curr:
            # print(curr.val)
            prev_val[curr] = prev
            prev = curr
            curr = prev.next
            n += 1

        reversed_head = prev
        print(n)

        for i in range(n//2):
            head_next = head.next
            head.next = reversed_head
            reversed_head.next = head_next
            reversed_head = prev_val[reversed_head]
            head = head_next
            if head == reversed_head or head_next == reversed_head:
                head.next = None 
                break
            if n % 2 == 0 and head_next:
                head_next.next = None
        