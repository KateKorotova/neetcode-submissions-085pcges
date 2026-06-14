# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        prev = ListNode()
        head = curr
        if not list1 or not list2:
            remaining = list1 if list1 else list2
            head = remaining
        while list1 and list2:
            if list1.val <= list2.val:
                curr.val = list1.val
                list1 = list1.next
            else:
                curr.val = list2.val
                list2 = list2.next
            prev.next = curr
            # curr.next = None
            prev = curr
            curr = ListNode()
        remaining = list1 if list1 else list2

        # print(remaining.val)
        if remaining:
            prev.next = remaining
        return head


