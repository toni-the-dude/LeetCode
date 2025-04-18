class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        freq = {}

        for candy in candyType:

            try:
                freq[candy] += 1
            except KeyError:
                freq[candy] = 1

        if len(freq) > len(candyType) // 2:
            return len(candyType) // 2
        return len(freq)