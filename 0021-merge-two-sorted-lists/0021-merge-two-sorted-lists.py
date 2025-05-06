# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None: return list2
        if list2 == None: return list1

        new_head = None
        ph = None
        p1 = list1
        p2 = list2

        while p1 != None and p2 != None:
            if new_head == None:
                if p1.val < p2.val:
                    ph = new_head = ListNode(p1.val, None)
                    p1 = p1.next
                else:
                    ph = new_head = ListNode(p2.val, None)
                    p2 = p2.next

            else:
                if p1.val < p2.val:
                    ph.next = ListNode(p1.val, None)
                    ph = ph.next
                    p1 = p1.next
                else:
                    ph.next = ListNode(p2.val, None)
                    ph = ph.next
                    p2 = p2.next

        if p1 == None and p2 != None:
            ph.next = p2
        elif p2 == None and p1 != None:
            ph.next = p1

        return new_head