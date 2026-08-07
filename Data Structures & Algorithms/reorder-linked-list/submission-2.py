# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = slow.next = None
        while curr:
            next_node = curr.next 
            curr.next = prev 
            prev = curr
            curr = next_node
        
        left = head 
        right = prev
        while left and right:
            left_next = left.next
            right_next = right.next
            left.next = right
            right.next = left_next

            left = left_next 
            right = right_next

        # return head

