# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return None

        reversed = ListNode(head.val, None)
        current = head

        while current.next != None:

            reversed = ListNode(current.next.val, reversed)
            current = current.next

        return reversed