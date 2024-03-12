class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        index = -2
        carry = 0
        
        digits[-1] = (digits[-1] + 1) % 10
        
        if digits[-1] == 0:
            carry = 1
        # print(carry)
        while index >= -len(digits):
            # print(digits[index])
            if carry == 1:
                digits[index] = (digits[index] + 1) % 10
                if digits[index] == 0:
                    carry = 1
                else:
                    carry = 0
            else:
                break
            
            index -= 1
            
        if carry == 1:
            digits.insert(0, 1)
            
        return digits