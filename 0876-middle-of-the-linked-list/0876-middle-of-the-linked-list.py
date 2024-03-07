# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        faster_head = head
        current_node = head
        
        while faster_head.next != None:
            if faster_head.next.next == None:
                return current_node.next
            faster_head = faster_head.next.next
            current_node = current_node.next
        
        return current_node