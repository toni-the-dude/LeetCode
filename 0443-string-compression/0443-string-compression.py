class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        count = 0
        prev_char = ""
        
        while len(chars) > 0:
            
            char = chars.pop(0)
            
            if count == 0:
                s += char
                count += 1
                
            elif prev_char == char:
                count += 1
                
            else:
                if count > 1:
                    s += str(count)
                count = 1
                s += char
                
            prev_char = char
        
        if count > 1:
            s += str(count)
        
        for i in range(0, len(s), 1):
            chars.append(s[i])
        
        return len(chars)
        