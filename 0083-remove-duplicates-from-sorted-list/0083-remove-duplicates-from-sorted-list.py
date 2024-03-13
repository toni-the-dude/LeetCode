# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None
        
        current_node = head
        
        while current_node.next != None:
            if current_node.val == current_node.next.val:
                try:
                    current_node.next = current_node.next.next
                except AttributeError:
                    current_node.next = None
            else:
                current_node = current_node.next
        
        return head