# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None: return False
        
        t = head
        h = head.next

        while t != h:
            try:
                t = t.next
                h = h.next.next
            except AttributeError: return False

        return True