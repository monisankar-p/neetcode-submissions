# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0

        while curr is not None:
            count += 1
            curr = curr.next

        temp = head
        prev = None

        for _ in range(count - n):
            prev = temp
            temp = temp.next

        if prev is None:
            return head.next
        prev.next = temp.next
        return head