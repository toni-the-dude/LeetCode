class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
        output = date.split("-")

        for i in range(0, len(output), 1):
            output[i] = bin(int(output[i]))[2:]
        
        return "-".join(output)