class Solution:
    def interpret(self, command: str) -> str:
        
        dict = {"G": "G", "()": "o", "(al)": "al"}
        output = ""
        current = ""

        for i in range(0, len(command), 1):
            current += command[i]
            if current not in dict: continue
            else: 
                output += dict[current]
                current = ""

        return output