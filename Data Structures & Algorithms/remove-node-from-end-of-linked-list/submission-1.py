# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []
        curr = head
        while curr:
            lst.append(curr)
            curr = curr.next
        remove_i = len(lst) - n

        if remove_i > 0:
            lst[remove_i - 1].next = lst[remove_i].next
            return lst[0]
        elif remove_i == 0 and len(lst) > 1:
            return lst[1]
        return None