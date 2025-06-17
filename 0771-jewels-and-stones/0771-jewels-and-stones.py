class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        dict_j = {}
        output = 0

        for j in jewels:
            dict_j[j] = 1

        for s in stones:
            if s in dict_j:
                output += 1

        return output