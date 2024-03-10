# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head = ListNode()
        
        carry = 0
        
        digit1 = l1
        digit2 = l2
        digits = sum_head # Current digit of sum
        # Initial step. The lists are non-empty
        digits = ListNode()
        sum_head = digits # Will be returned at the end
        
        digits.val = (digit1.val + digit2.val + carry) % 10
        carry = (digit1.val + digit2.val + carry) // 10
            
        digit1 = digit1.next 
        digit2 = digit2.next
        
        while digit1 != None and digit2 != None:
            digits.next = ListNode() # Create more nodes for the sum as needed
            digits = digits.next
            
            digits.val = (digit1.val + digit2.val + carry) % 10 # Addition
            carry = (digit1.val + digit2.val + carry) // 10
            
            digit1 = digit1.next # Iteration
            digit2 = digit2.next
            
        while digit1 != None: 
            # print("l1 not finished")
            digits.next = ListNode() # Creation
            digits = digits.next
            
            digits.val = (digit1.val + carry) % 10 # Addition
            carry = (digit1.val + carry) // 10
            
            digit1 = digit1.next # Iteration
            
        while digit2 != None:
            # print("l2 not finished")
            digits.next = ListNode() # Creation
            digits = digits.next
            
            digits.val = (digit2.val + carry) % 10 # Addition
            carry = (digit2.val + carry) // 10
            
            digit2 = digit2.next # Iteration
            
        if carry != 0:
            digits.next = ListNode()
            digits = digits.next
            
            digits.val = carry
            
        return sum_head