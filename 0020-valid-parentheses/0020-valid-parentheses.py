class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for bracket in s:
            if bracket in ['(', '[', '{']:
                stack.append(bracket)
            else: # In ASCII, '(' is 40, ')' is 41, '[' is 91, ']' is 93, '{' is 123 and '}' is 125             
                try:
                    if stack[-1] == chr(ord(bracket) - 1) or stack[-1] == chr(ord(bracket) - 2): 
                        stack.pop()
                    else:
                        return False
                except IndexError:
                    return False
                
        if stack == []:
            return True

        return False