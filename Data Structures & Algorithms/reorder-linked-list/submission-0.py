# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return 

        values = []
        curr = head

        while curr is not None:
            values.append(curr)
            curr=curr.next
        i = 0
        j = len(values) - 1
        k = 0

        dummy = ListNode()
        curr = dummy

        while i <= j:
            if k % 2 != 0:
                curr.next = values[j]
                j -= 1
            else:
                curr.next = values[i]
                i += 1
            k += 1
            curr = curr.next

        curr.next = None

        

        