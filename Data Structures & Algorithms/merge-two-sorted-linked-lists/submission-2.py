# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        if list1 is None and list2 is None:
            return None

        values = []
        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                values.append (curr1.val)
                curr1 = curr1.next

            else:
                values.append(curr2.val)
                curr2 = curr2.next

        while curr1 is not None:
            values.append (curr1.val)
            curr1 = curr1.next

        while curr2 is not None:
            values.append (curr2.val)
            curr2 = curr2.next

        head = ListNode(values[0])
        curr = head
        for i in range(1, len(values)):
            new_node = ListNode(values[i])
            curr.next = new_node
            curr = curr.next

        return head