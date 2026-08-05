# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return 

        values = []
        curr = head

        while curr is not None:
            values.append(curr.val)
            curr = curr.next
        
        i = 0
        j = len(values) - 1

        result = []

        while i <= j:
            if i == j:
                result.append(values[i])
            else:
                result.append(values[i])
                result.append(values[j])
            i += 1
            j -= 1

        curr = head
        for res in result:
            curr.val = res
            curr = curr.next

        

        