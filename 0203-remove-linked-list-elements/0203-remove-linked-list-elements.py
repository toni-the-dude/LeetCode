# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head != None and head.val == val:
            head = head.next

        current_node = head

        while current_node != None:
            if current_node.next != None and current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return head