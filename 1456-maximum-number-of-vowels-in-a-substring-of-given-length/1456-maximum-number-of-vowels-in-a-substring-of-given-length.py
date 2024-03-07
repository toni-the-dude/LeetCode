class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        max_vow = 0
        current_vow = 0
        head = 0
        tail = 0
        
        while head < k:
            if s[head] in "aeiou":
                current_vow += 1
            head += 1
            
        head -= 1
        max_vow = current_vow
        
        while head < len(s):
            
            if s[tail] in "aeiou":
                current_vow -= 1
                
            tail += 1
            head += 1
            
            if head != len(s):
                if s[head] in "aeiou":
                    current_vow += 1
                
            if current_vow > max_vow:
                max_vow = current_vow
        
        return max_vow